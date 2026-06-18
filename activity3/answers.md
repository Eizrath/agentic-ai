# Activity 3: Simulated Tool Use (ReAct)

## Screenshots

Saved the screenshots of the output inside the `screenshots/` folder.

---

## 1. Did the agent output `TOOL: get_weather('Manila')`?

Yep. The agent figured out that it needed weather information first before answering the question, so instead of jumping straight to an answer, it requested:

```text
TOOL: get_weather(Manila)
```

Basically, it understood that it was missing some information and decided to use the appropriate tool. So the ReAct flow worked as intended.

---

## 2. Did the final answer incorporate the `32°C` data?

Yep. After receiving the observation:

```text
OBSERVATION: The temperature in Manila is 32°C and sunny.
```

the final answer became:

> "It's 32°C and sunny in Manila today, so I recommend wearing light and breathable clothing."

So the answer wasn't just made up. It actually used the information returned by the simulated weather tool, which is pretty much the whole point of ReAct.

---

## 3. Reflection: Why did we have to send `[user_query, response.text, observation]` as a list in Turn 2?

Think of it like giving the model a recap of what just happened. The model doesn't magically remember everything from the previous call, so we had to send the whole context back.

* `user_query` reminds it what the user originally asked.
* `response.text` tells it which action it decided to take.
* `observation` gives it the result from that action.

Without all three, the model would just see some random weather data and have no clue why it received it. Sending them together basically lets the model connect the dots and come up with a sensible answer.

Overall, the ReAct pattern worked pretty nicely. The agent first thought about what information it needed, requested a tool, got the data, and then used that data to answer the question. In a way, we're manually acting as the "environment" and feeding the agent the information it needs to finish the job.
