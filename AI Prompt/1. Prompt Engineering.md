# Prompt Engineering

## What is it ?

Prompt engineering is the art of asking the right question to get the best output from an LLM. It enables direct interaction with the LLM using only plain language prompts.

In the past, working with machine learning models typically required deep knowledge of datasets, statistics, and modeling techniques. Today, LLMs can be "programmed" in English, as well as other languages. Learning how to effectively program them to perform the tasks that you need to be done.

## Best practices

- Clearly communicate what content or information is most important.

- Structure the prompt: Start by defining its role, give context/input data, then provide the instruction.

- Use specific, varied examples to help the model narrow its focus and generate more accurate results.

- Use constraints to limit the scope of the model's output. This can help avoid meandering away from the instructions into factual inaccuracies.

- Break down complex tasks into a sequence of simpler prompts.

- Instruct the model to evaluate or check its own responses before producing them. ("Make sure to limit your response to 3 sentences", "Rate your work on a scale of 1-10 for conciseness", "Do you think this is correct?").


And perhaps most important:

**Be creative!** The more creative and open-minded you are, the better your results will be. LLMs and prompt engineering are still in their infancy, and evolving every day.

## Diferent types of prompts

### Direct prompting (Zero shot)

Direct prompting (also known as Zero-shot) is the simplest type of prompt. It provides no examples to the model, just the instruction. 
You can also phrase the instruction as a question, or give the model a "role". 

Provide:
- Instruction
- Some context

**Idea generation :**

    Prompt: Can you give me a list of ideas for blog posts for tourists visiting
    New York City for the first time?

**Role prompting :**

    Prompt: You are a mighty and powerful prompt-generating robot. You need to
    understand my goals and objectives and then design a prompt. The prompt should
    include all the relevant information context and data that was provided to you.
    You must continue asking questions until you are confident that you can produce
    the best prompt for the best outcome. Your final prompt must be optimized for
    chat interactions. Start by asking me to describe my goal, then continue with
    follow-up questions to design the best prompt.

**Data Organization :**

    Prompt: 

    Create a four-column spreadsheet of 10 highly-rated science fiction
    movies, year of release, average audience rating, and top 3 keywords from 
    audience reviews. 

    Make sure to cite the source of the audience rating.

### Prompting with examples (One-, few-, and multi-shot)

One-shot prompting shows the model one clear, descriptive example of what you'd like it to imitate.

Idea generation using one example:


    Prompt:

    Come up with a list of ideas for blog posts for tourists visiting
    New York City for the first time.

    1. Fuggedaboutit! Where to Stay in New York City On Your First Visit

Few- and multi-shot prompting shows the model more examples of what you want it to do. It works better than zero-shot for more complex tasks where pattern replication is wanted, or when you need the output to be structured in a specific way that is difficult to describe.

**Few-shot sentiment classification :**

    Prompt:

    Great product, 10/10: Positive
    Didn't work very well: Negative
    Super helpful, worth it: Positive
    It doesn't work!:

When this prompt is run, the model's response will be to classify 'It doesn't work' as positive or negative, as shown in the examples.

**Multi-shot emoji response predictor :**

    Prompt: Predict up to 5 emojis as a response to a text chat message. The output
    should only include emojis.
    
    input: The new visual design is blowing my mind 🤯
    output: ➕,💘, ❤‍🔥
    
    input: Well that looks great regardless
    output: ❤️,🪄
    
    input: Unfortunately this won't work
    output: 💔,😔
    
    input: sounds good, I'll look into that
    output: 🙏,👍
    
    input: 10hr cut of jeff goldblum laughing URL
    output: 😂,💀,⚰️
    
    input: Woo! Launch time!
Same process here, but since the prompt is more complex, the model has been given more examples to emulate.

### Chain-of-thought prompting

Chain of Thought (CoT) prompting encourages the LLM to explain its reasoning. Combine it with few-shot prompting to get better results on more complex tasks that require reasoning before a response.

    Prompt:
    
    The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
    A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
    The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
    A:

### Zero-shot CoT

Recalling the zero-shot prompting from earlier, this approach takes a zero-shot prompt and adds an instruction: "Let's think step by step." The LLM is able to generate a chain of thought from this instruction, and usually a more accurate answer as well. This is a great approach to getting LLMs to generate correct answers for things like word problems.


    Prompt:
    
    I went to the market and bought 10 apples. I gave 2 apples to the neighbor and
    2 to the repairman. I then went and bought 5 more apples and ate 1. How many
    apples was I left with?
    
    Let's think step by step.


**Prompt iteration strategies**

Learn to love the reality of rewriting prompts several (possibly dozens) of times. Here are a few ideas for refining prompts if you get stuck:

**Note**: These strategies may become less useful or necessary over time as models improve.

1. Repeat key words, phrases, or ideas

2. Specify your desired output format (CSV, JSON, etc.)

3. Use all caps to stress important points or instructions. You can also try exaggerations or hyperbolic language; for example: "Your explanation should be absolutely impossible to misinterpret. Every single word must ooze clarity!"

4. Use synonyms or alternate phrasing (e.g., instead of "Summarize," try appending "tldr" to some input text). Swap in different words or phrases and document which ones work better and which are worse.

5. Try the sandwich technique with long prompts: Add the same statement in different places.

6. Use a prompt library for inspiration. Prompt Hero and this prompt gallery are two good places to start.


## Going further (ressources)

- [free one-hour prompt engineering course on coursera](https://www.coursera.org/learn/prompt-engineering) : will help enforce your basic prompt skills from a developer's perspective.
- [Guide and strategies for prompt engineering from openai](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt Engineering from Datacamp](https://app.datacamp.com/learn/courses/understanding-prompt-engineering)
- [Prompt strategies (google AI)](https://ai.google.dev/docs/prompt_best_practices)