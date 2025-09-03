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
