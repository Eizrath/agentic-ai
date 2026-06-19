# Part I: Code Debugging/Correction (10 Points)

### 1. The Stateless Loop (2 pts)

**Error:**  
`chat = client.chats.create(model="gemini-3.1-flash-lite")` is inside the while loop. It creates a new chat everytime the user interacts so the chat history is wiped out and not saved.

**Fix:**  
```python
chat = client.chats.create(model="gemini-3.1-flash-lite") # Line A

while True:   
    user_input = input("> ")
    response = chat.send_message(user_input)
    print(response.text)
```

### 2. The Leaky Identity (2 pts)

**Error:**  
The description `"Be helpful"`, conflicts with the user's constraint or prompt and the model prioritizes helpfulness over the prompt, so it just answers directly.

**Fix (System Instruction):**  
```python
identity = "You are a math tutor. Never reveal direct answers. Only provide hints, steps, or guiding questions to help the student come up with the answers themselves."
```


### 3. The Memory Bloat (2 pts)

**Error:**  
`chat.history[0]` returns a single message object, not a list. Assigning a non-list to chat.history corrupts it and doesn't actually prune correctly.

**Fix (Line B):**  
```python
chat.history = chat.history[-2:]
```

### 4. The Perception Crash (2 pts)

**Error:**  
`price: float` is required with no default value. So when the LLM runs it, the response.parsed is missing the field and the constructor crashes with a ValidationError.

**Fix (Pydantic Model):**  
```python
class Item(BaseModel):
    name: str
    price: Optional[float] = None
```

### 5. The Infinite Backoff (2 pts)
5. The Infinite Backoff

**Error:**  
The `else` block calls continue on all other exceptions (401, 403, etc.), causing infinite retries even when retrying is pointless.

**Fix (Else Block):**  
```python
else:
    raise
```

---

# Part II: Schema Design & Evaluation (10 Points)

## Task 1: The Multi-Agent Router (5 Points)

### Pydantic Schema

```python
from pydantic import BaseModel, Field
from enum import Enum

class Department(str, Enum):
    PAYROLL = "PAYROLL"
    RECRUITING = "RECRUITING"
    LEAVE_REQUEST = "LEAVE_REQUEST"

class HRPydanticSchema(BaseModel):
    department: Department = Field(
        description="The HR department best suited to handle this request."
    )
    reasoning: str = Field(
        description="Step-by-step chain of thought explaining why this department was chosen."
    )
    urgency_level: int = Field(
        ge=1, le=5,
        description="Urgency score from 1 (low) to 5 (critical)."
    )

```

---

## Task 2: Architecture Evaluation (5 Points)
Arch B is the obvious winner for a 24/7 production system.  
A 5,000-word static prompt sounds thorough until you realize you're blasting that entire token load on every single one of 500 daily calls and the cost alone should kill Arch A immediately.  
On top of that, raw text output at that volume will malform eventually, and Arch A has zero recovery plan when it does.  
Arch B's Pydantic schema catches bad output via ValidationError and self-corrects automatically, while the 3-turn Sliding Window keeps each call lean and cheap.  
One architecture trusts the LLM blindly and pays for it(Arch A), the other expects failure and handles it gracefully(Arch B).  
