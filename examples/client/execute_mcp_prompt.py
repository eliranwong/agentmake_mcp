import asyncio, pprint, re
from fastmcp import Client
from agentmake import agentmake

client = Client("http://127.0.0.1:8080/mcp/")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available tools, resources, and prompts
        tools = await client.list_tools()
        tools = {t.name: t.description for t in tools}
        print("# Tools\n\n", tools, "\n\n")
        resources = await client.list_resources()
        print("# Resources\n\n", resources, "\n\n")
        prompts = await client.list_prompts()
        print("# Prompts\n\n", prompts, "\n\n")
        
        # Call a tool
        #result = await client.call_tool("ask_chatgpt", {"request": "What is AI?"})
        #print(result, "\n\n")
        #mcp_response = result.content[0].text
        #print(mcp_response, "\n\n")

        # Call a MCP prompt
        result = await client.get_prompt("ask_multiple_models", {"request": "What is AI?"})
        #print(result, "\n\n")
        mcp_prompt = result.messages[0].content.text
        print(mcp_prompt)

        system_suggestion = f"""

You are a supervisor overseeing if multiple steps instructions, givent in the `Master Prompt`, are followed correctly.
The ovverall goal is to ensure that the `Original Request` specified in the `Master Prompt` is completely resolved, and a concise summary is provided at the end.
Carefully check the progress of the conversation, and provide suggestions in the next response, according to `Guidelines for Making Suggestions`.

# Master Prompt

{mcp_prompt}

# Guidelines for Making Suggestions

Here are guidlines for making suggestions in the next response

* Please follow the steps in the master prompt one by one
* If all the steps are completed, please provide a concise summary
* Reply in one word "DONE" in capital letters when all the steps are completed and a concise summary is provided.
"""
        
        
        available_tools = list(tools.keys())
        if not "get_direct_text_response" in available_tools:
            available_tools.insert(0, "get_direct_text_response")

        system_tool_selection = f"""You are an expert in selecting the most appropriate AI tools to address a given suggestion. Your task is to analyze the suggestion and choose the best-suited tool from a list of available tools, i.e. {available_tools}. You will be provided with the `TOOL DESCRIPTION` of each tool below. Consider the strengths and capabilities of each tool in relation to the suggestion at hand. Ensure your choice aligns with the goal of effectively addressing the suggestion. After your analysis, reoder the list of available tools from the most relevant to the least relevant, and provide your response in the python list format, without any additional commentary or explanation. Refer to the `OUTPUT FORMAT` section below for the expected format of your response.
        

        """

        if not "get_direct_text_response" in tools:
            system_tool_selection += f"""# TOOL DESCRIPTION: `get_direct_text_response`
Get a text-based response directly from a text-based AI model without using any other tools. This is useful when you want to provide a simple and direct answer to a question or request, without the need for online latest updates or task execution.


"""

        for tool_name, tool_description in tools.items():
            system_tool_selection += f"""# TOOL DESCRIPTION: `{tool_name}`
{tool_description}


"""
        system_tool_selection += """# OUTPUT FORMAT
Your response should be in the following python list format:
["most_relevant_tool", "second_most_relevant_tool", "third_most_relevant_tool", "...", "least_relevant_tool"]

Remember to only provide the python list as your response, without any additional commentary or explanation."""


        system_instruction = """You are an expert giving instructions to an AI assistant to help it achieve a specific goal. You will be provided with the suggestion from the supervisor, and you need to convert it into clear and concise instructions for the AI assistant to follow. You provide the converted instruction directly, without any additional commentary or explanation."""

        def get_system_tool_instruction(selected_tool):
            return f"""You are an expert in converting suggestions into clear and concise instructions for an AI assistant to follow. You will be provided with the suggestion from the supervisor, and you need to convert it into clear and concise instructions for the AI assistant to follow, using the specified tool `{selected_tool}`. 
            
            Formate your response as a direct request to the AI assistant, specifying information that the tool `{selected_tool}` requires to complete the task, according to the tool's description: 
            
            ```tool description
            {tools.get(selected_tool, "No description available.")}
            ```

            Remember:
            * Do not mention the tool name in your instruction.
            * Do not mention further steps or tools to be used after this instruction.
            * Only provide the instruction for the specified tool `{selected_tool}`.

            You provide the converted instruction directly, without any additional commentary or explanation."""

        original_request = "What is AI?"
        messages_init = agentmake(original_request, system=system_suggestion)
        
        # Extract the first suggestion
        first_suggestion = messages_init[-1].get("content", "").strip()
        # Extract suggested tools from the first suggestion
        suggested_tools = agentmake(first_suggestion, system=system_tool_selection)[-1].get("content", "").strip()
        suggested_tools = re.sub(r"^.*?(\[.*?\]).*?$", r"\1", suggested_tools, flags=re.DOTALL)
        suggested_tools = eval(suggested_tools) if suggested_tools.startswith("[") and suggested_tools.endswith("]") else ["get_direct_text_response"] # fallback to direct response
        # Use the first suggested tool
        first_tool = suggested_tools[0] if suggested_tools else "get_direct_text_response"
        if first_tool == "get_direct_text_response":
            first_step = agentmake(first_suggestion, system=system_instruction)[-1].get("content", "").strip()
        else:
            first_step = agentmake(first_suggestion, system=get_system_tool_instruction(first_tool))[-1].get("content", "").strip()

        messages = [
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": original_request},
            {"role": "assistant", "content": "Please provide me with an initial instruction to begin."},
            {"role": "user", "content": first_step},
        ]

        if first_tool == "get_direct_text_response":
            messages = agentmake(messages)
        else:
            tool_result = await client.call_tool(first_tool, {"request": first_step})
            tool_result = tool_result.content[0].text
            messages[-1]["content"] += f"\n\n[Using tool `{first_tool}`]"
            messages.append({"role": "assistant", "content": tool_result})

        next_suggestion = agentmake(messages, system=system_suggestion, follow_up_prompt="Please provide the next suggestion.")[-1].get("content", "").strip()

        n = 0

        while not "DONE" in next_suggestion:

            # Extract suggested tools from the next suggestion
            suggested_tools = agentmake(next_suggestion, system=system_tool_selection)[-1].get("content", "").strip()
            suggested_tools = re.sub(r"^.*?(\[.*?\]).*?$", r"\1", suggested_tools, flags=re.DOTALL)
            suggested_tools = eval(suggested_tools) if suggested_tools.startswith("[") and suggested_tools.endswith("]") else ["get_direct_text_response"] # fallback to direct response
            # TODO: check if the suggested tools are in available_tools
            # Use the next suggested tool
            next_tool = suggested_tools[0] if suggested_tools else "get_direct_text_response"
            if next_tool == "get_direct_text_response":
                next_step = agentmake(next_suggestion, system=system_instruction)[-1].get("content", "").strip()
            else:
                next_step = agentmake(next_suggestion, system=get_system_tool_instruction(next_tool))[-1].get("content", "").strip()

            messages.append({"role": "user", "content": next_step})

            if next_tool == "get_direct_text_response":
                messages = agentmake(messages)
            else:
                tool_result = await client.call_tool(next_tool, {"request": next_step})
                tool_result = tool_result.content[0].text
                messages[-1]["content"] += f"\n\n[Using tool `{next_tool}`]"
                messages.append({"role": "assistant", "content": tool_result})

            next_suggestion = agentmake(messages, system=system_suggestion, follow_up_prompt="Please provide me with the next suggestion.")[-1].get("content", "").strip()
            
            n += 1
            if n > 5:
                print("Error! Too many iterations!")
                break

        pprint.pprint(messages)

asyncio.run(main())

# Output:
"""
# Tools

 {'ask_chatgpt': 'Ask ChatGPT', 'ask_grok': 'Ask Grok', 'ask_claude': 'Ask Claude', 'ask_gemini': 'Ask Gemini'} 


# Resources

 [] 


# Prompts

 [Prompt(name='ask_multiple_models', title=None, description='Ask multiple AI models at once', arguments=[PromptArgument(name='request', description=None, required=True)], meta={'_fastmcp': {'tags': []}})] 


You are a moderator in a collaborative discussion. Your goal is to pass the original request to different AI models for reviews and summarize the results.
    
Please perform the following steps in order:
1. Call the tool `ask_chatgpt` to answer the request.
2. Call the tool `ask_grok` to answer the request.
3. Call the tool `ask_claude` to answer the request.
4. Call the tool `ask_gemini` to answer the request.
5. Compare the reviews.
6. Summarize the results.


# Here is the request:
---
What is AI?
---

You have only asked the question from the **Original Request** ("What is AI?"),
but according to the **Master Prompt**, you still need to:

1. Call `ask_chatgpt` to answer the request.
2. Call `ask_grok` to answer the request.
3. Call `ask_claude` to answer the request.
4. Call `ask_gemini` to answer the request.
5. Compare the reviews from all four tools.
6. Summarize the results concisely.

**Suggestion:**
Proceed with step 1 by calling `ask_chatgpt` and getting its answer to "What is
AI?" before moving to the next steps.

["ask_chatgpt", "ask_grok", "ask_claude", "ask_gemini",
"get_direct_text_response"]

Provide a clear and concise explanation of "What is AI?" including its
definition, key concepts, and common applications.

The next step is to call the tool **`ask_grok`** to answer the same request —
providing a clear and concise explanation of "What is AI?" including its
definition, key concepts, and common applications — so we can proceed with
gathering multiple perspectives for comparison.

["ask_grok", "ask_chatgpt", "ask_claude", "ask_gemini",
"get_direct_text_response"]

Provide a clear and concise explanation of "What is AI?" including its
definition, key concepts, and common applications.

The next step is to call the tool **`ask_claude`** to answer the same request —
provide a clear and concise explanation of "What is AI?" including its
definition, key concepts, and common applications.

["ask_claude", "ask_chatgpt", "ask_gemini", "ask_grok",
"get_direct_text_response"]

Provide a clear and concise explanation of "What is AI?" including its
definition, key concepts, and common applications.

You have completed steps 1–3 (ask_chatgpt, ask_grok, ask_claude).
The next step according to the master prompt is:

**Step 4:** Call the tool `ask_gemini` to answer the request:
> Provide a clear and concise explanation of "What is AI?" including its
definition, key concepts, and common applications.

["ask_gemini", "ask_chatgpt", "ask_claude", "ask_grok",
"get_direct_text_response"]

Provide a clear and concise explanation of "What is AI?" including its
definition, key concepts, and common applications.

You have now completed steps 1–4 of the Master Prompt by gathering responses
from `ask_chatgpt`, `ask_grok`, `ask_claude`, and `ask_gemini`.

The next step is **Step 5: Compare the reviews** — analyze the similarities and
differences in their definitions, key concepts, and applications of AI.

After that, proceed to **Step 6: Summarize the results** into a concise, clear
overview that captures the common points and any notable differences.

Once you’ve done that, if the summary fully resolves the original request, you
should reply with **"DONE"**.

[{'content': 'You are an AI assistant.', 'role': 'system'},
 {'content': 'What is AI?', 'role': 'user'},
 {'content': 'Please provide me with an initial instruction to begin.',
  'role': 'assistant'},
 {'content': 'Provide a clear and concise explanation of "What is AI?" '
             'including its definition, key concepts, and common '
             'applications.\n'
             '\n'
             '[Using tool `ask_chatgpt`]',
  'role': 'user'},
 {'content': '**What is AI?**  \n'
             '\n'
             '**Definition:**  \n'
             'Artificial Intelligence (AI) is the field of computer science '
             'focused on creating systems or machines that can perform tasks '
             'that normally require human intelligence. These tasks include '
             'learning, reasoning, problem-solving, understanding language, '
             'and perceiving the environment.\n'
             '\n'
             '**Key Concepts:**  \n'
             '1. **Machine Learning (ML):** A subset of AI where algorithms '
             'learn patterns from data and improve over time without being '
             'explicitly programmed.  \n'
             '2. **Neural Networks:** Computational models inspired by the '
             'human brain, used for recognizing patterns and making '
             'predictions.  \n'
             '3. **Natural Language Processing (NLP):** Enables machines to '
             'understand, interpret, and respond to human language.  \n'
             '4. **Computer Vision:** The ability of machines to interpret and '
             'process visual information from the world.  \n'
             '5. **Robotics:** The integration of AI into machines that can '
             'interact with the physical environment.  \n'
             '\n'
             '**Common Applications:**  \n'
             '- **Virtual Assistants** (e.g., Siri, Alexa, Google '
             'Assistant)  \n'
             '- **Recommendation Systems** (e.g., Netflix, Amazon product '
             'suggestions)  \n'
             '- **Autonomous Vehicles** (self-driving cars)  \n'
             '- **Fraud Detection** in banking and finance  \n'
             '- **Medical Diagnosis** and imaging analysis  \n'
             '- **Chatbots** for customer service  \n'
             '- **Smart Home Devices** (e.g., AI-powered thermostats, security '
             'systems)  \n'
             '\n'
             'If you’d like, I can also create a **simple visual diagram** '
             'showing AI’s definition, core concepts, and applications for '
             'quick reference. Would you like me to prepare that?',
  'role': 'assistant'},
 {'content': 'Provide a clear and concise explanation of "What is AI?" '
             'including its definition, key concepts, and common '
             'applications.\n'
             '\n'
             '[Using tool `ask_grok`]',
  'role': 'user'},
 {'content': 'AI, or Artificial Intelligence, refers to the development of '
             'computer systems that can perform tasks typically requiring '
             'human intelligence. These tasks include learning, reasoning, '
             'problem-solving, understanding natural language, and perceiving '
             'the environment.\n'
             '\n'
             '**Key Concepts of AI:**\n'
             '- **Machine Learning (ML):** A subset of AI where systems learn '
             'from data to improve their performance over time without being '
             'explicitly programmed.\n'
             "- **Neural Networks:** Algorithms inspired by the human brain's "
             'structure, used in tasks like image and speech recognition.\n'
             '- **Natural Language Processing (NLP):** Enables machines to '
             'understand and generate human language, as seen in chatbots and '
             'translation tools.\n'
             '- **Computer Vision:** Allows AI to interpret and process visual '
             'information, such as identifying objects in images or videos.\n'
             '- **Robotics:** Combines AI with physical systems to create '
             'machines that can perform tasks autonomously or '
             'semi-autonomously.\n'
             '\n'
             '**Common Applications of AI:**\n'
             '- **Virtual Assistants:** Tools like Siri and Alexa that help '
             'with daily tasks through voice commands.\n'
             '- **Recommendation Systems:** Used by platforms like Netflix and '
             'Amazon to suggest content or products based on user '
             'preferences.\n'
             '- **Healthcare:** AI aids in diagnosing diseases, personalizing '
             'treatments, and analyzing medical images.\n'
             '- **Autonomous Vehicles:** Self-driving cars use AI to navigate '
             'and make real-time decisions.\n'
             '- **Finance:** AI detects fraud, automates trading, and assesses '
             'credit risks.\n'
             '\n'
             'In essence, AI is about creating systems that mimic human '
             'cognitive abilities, transforming industries and everyday life '
             'through automation and intelligent decision-making.',
  'role': 'assistant'},
 {'content': 'Provide a clear and concise explanation of "What is AI?" '
             'including its definition, key concepts, and common '
             'applications.\n'
             '\n'
             '[Using tool `ask_claude`]',
  'role': 'user'},
 {'content': "Here's a clear explanation of AI:\n"
             '\n'
             'Definition:\n'
             'Artificial Intelligence (AI) is the simulation of human '
             'intelligence by machines, enabling them to learn from '
             'experience, adapt to new information, and perform human-like '
             'tasks.\n'
             '\n'
             'Key Concepts:\n'
             '1. Machine Learning\n'
             '- Systems that improve through experience\n'
             '- Learn patterns from data without explicit programming\n'
             '- Examples: Netflix recommendations, spam filters\n'
             '\n'
             '2. Deep Learning\n'
             '- Advanced AI using neural networks\n'
             '- Processes complex patterns\n'
             '- Examples: Face recognition, language translation\n'
             '\n'
             '3. Natural Language Processing\n'
             '- Enables machines to understand human language\n'
             '- Used in chatbots and virtual assistants\n'
             '- Examples: Siri, Alexa\n'
             '\n'
             'Common Applications:\n'
             '• Healthcare (disease diagnosis, drug discovery)\n'
             '• Finance (fraud detection, trading)\n'
             '• Transportation (self-driving cars)\n'
             '• Entertainment (gaming, content recommendations)\n'
             '• Business (customer service, process automation)\n'
             '• Smart homes (IoT devices, security systems)\n'
             '\n'
             'AI continues to evolve rapidly, transforming industries and '
             'daily life through automation and intelligent decision-making '
             'capabilities.',
  'role': 'assistant'},
 {'content': 'Provide a clear and concise explanation of "What is AI?" '
             'including its definition, key concepts, and common '
             'applications.\n'
             '\n'
             '[Using tool `ask_gemini`]',
  'role': 'user'},
 {'content': 'Of course. Here is a clear and concise explanation of Artificial '
             'Intelligence.\n'
             '\n'
             '### What is Artificial Intelligence (AI)?\n'
             '\n'
             'At its core, **Artificial Intelligence (AI)** is a broad field '
             'of computer science dedicated to creating machines or systems '
             'that can perform tasks that normally require human intelligence. '
             'This includes abilities like learning from experience, '
             'reasoning, solving problems, understanding language, and '
             'perceiving the environment.\n'
             '\n'
             'The ultimate goal of AI is not just to mimic human intelligence, '
             'but to create tools that can augment and extend our own '
             'capabilities.\n'
             '\n'
             '---\n'
             '\n'
             '### Key Concepts\n'
             '\n'
             'AI is not a single technology but a collection of different '
             'methods and subfields. The most important concepts to understand '
             'are:\n'
             '\n'
             '1.  **Machine Learning (ML):** This is the most common type of '
             'AI in use today. Instead of being explicitly programmed with '
             'rules for a task, an ML system is **trained on large amounts of '
             'data**. It learns to recognize patterns and make predictions or '
             'decisions based on that data.\n'
             "    *   **Example:** A spam filter isn't programmed with a list "
             "of every possible spam word. Instead, it's trained on millions "
             'of emails, learning the features that distinguish spam from '
             'legitimate messages.\n'
             '\n'
             '2.  **Deep Learning:** A powerful subfield of Machine Learning '
             'that uses complex, multi-layered structures called **neural '
             "networks**. These networks are inspired by the human brain's "
             'structure and are exceptionally good at finding intricate '
             'patterns in massive datasets.\n'
             '    *   **Example:** Deep learning powers image recognition '
             '(like identifying a cat in a photo) and the advanced language '
             'understanding of models like ChatGPT.\n'
             '\n'
             '3.  **Neural Networks:** These are the computing systems at the '
             'heart of Deep Learning. They consist of interconnected nodes, or '
             '"neurons," organized in layers. Each layer processes information '
             'and passes it to the next, allowing the network to learn '
             'progressively more complex features from the data.\n'
             '\n'
             '4.  **Natural Language Processing (NLP):** This is the branch of '
             'AI that gives machines the ability to read, understand, '
             "interpret, and generate human language. It's the bridge between "
             'human communication and computer understanding.\n'
             '    *   **Example:** Virtual assistants like Siri and Alexa, '
             'Google Translate, and customer service chatbots all rely on '
             'NLP.\n'
             '\n'
             '5.  **Computer Vision:** This field enables machines to "see" '
             'and interpret visual information from the world, such as images '
             'and videos.\n'
             '    *   **Example:** Facial recognition on your phone, '
             'self-driving cars identifying pedestrians and traffic signs, and '
             'medical systems analyzing X-rays.\n'
             '\n'
             '---\n'
             '\n'
             '### Common Applications\n'
             '\n'
             'AI is already integrated into many aspects of our daily lives '
             'and industries:\n'
             '\n'
             '| Category | Application Examples |\n'
             '| :--- | :--- |\n'
             '| **Everyday Life** | **Recommendation Engines:** Netflix, '
             'Spotify, and Amazon suggesting what you might like '
             'next.<br>**Virtual Assistants:** Siri, Google Assistant, and '
             'Alexa answering questions and performing '
             'tasks.<br>**Navigation:** Google Maps and Waze calculating the '
             'fastest routes by analyzing real-time traffic data. |\n'
             '| **Business & Finance** | **Customer Service:** AI-powered '
             'chatbots providing 24/7 support.<br>**Fraud Detection:** Banks '
             'using AI to identify unusual transaction patterns and prevent '
             'fraud.<br>**Supply Chain Optimization:** Predicting demand and '
             'managing inventory more efficiently. |\n'
             '| **Healthcare** | **Medical Imaging:** Analyzing MRIs, CT '
             'scans, and X-rays to detect diseases like cancer earlier and '
             'more accurately.<br>**Drug Discovery:** Accelerating research by '
             'analyzing complex biological data to find new potential '
             'treatments. |\n'
             '| **Creative & Entertainment** | **Generative AI:** Creating '
             'original text (ChatGPT), images (Midjourney, DALL-E), and music '
             'from simple prompts.<br>**Gaming:** Creating smarter, more '
             "realistic non-player characters (NPCs) that adapt to a player's "
             'actions. |\n'
             '| **Transportation** | **Autonomous Vehicles:** Self-driving '
             'cars and trucks that use sensors and computer vision to navigate '
             'roads.<br>**Driver-Assist Systems:** Features like adaptive '
             'cruise control and automatic emergency braking. |',
  'role': 'assistant'}]
"""