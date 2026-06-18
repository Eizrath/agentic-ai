# Activity 2: Goal-Driven Autonomy

## ITE04

# Activity 2: Autonomous Pla

Place the screenshots of the program output inside the `screenshots/` folder.

Example structure:

```
activity2/
│
├── app.py
├── answers.md
└── screenshots/
    ├── output_3_steps.png
    └── output_5_steps.png
```

---

## 1. Did the agent stay focused on the goal throughout the loop?

Yeah. The agent stayed pretty consistent with the original goal, which was to deploy a secure web application for a small business. Every step it generated was still related to that objective, and it followed a logical order from planning, development, testing, and finally deployment. It didn't suddenly go off-topic or produce unrelated tasks, so overall it stayed focused throughout the loop.

---

## 2. Challenge: Modify the loop to perform 5 steps instead of 3. How does this affect the detail of the plan?

Modifying the loop to perform 5 steps instead of 3 resulted in a more detailed plan, instead of combining multiple tasks into a few broad stages, the agent separated the process into smaller, more specific and detailed plans/actions.

### Output with 3 Steps

1. Define functional and security requirements, select technology stack, and design the application architecture.
2. Develop the application, implement security features and best practices, and conduct comprehensive testing (functional, performance, and security)
3. Provision production infrastructure, deploy the application with hardened security configurations, and establish ongoing monitoring and maintenance protocols.

### Output with 5 Steps

1. Define application functional and security requirements, select technology stack, and plan architecture.
2. Develop the application, implement secure coding practices, and establish a secure database structure
3. Conduct thorough application testing (functional, performance, security, and penetration testing) and provision/configure the production server infrastructure with necessary security controls.
4. Implement application production configurations, establish external network security (e.g., DNS, WAF, load balancers), set up comprehensive monitoring and logging systems, and perform a final pre-deployment security review.
5. Execute the deployment plan, migrate the application to the production environment, perform post-deployment functional and security validation, and transition to operational support with established incident response and continuous monitoring.

### Observation

With only 3 steps, the agent gave a broad overview of the process by grouping several tasks together. For example, development and testing were combined into a single stage.

When I increased it to 5 steps, the agent started breaking things down into smaller and more specific tasks. It added extra details such as configuring server infrastructure, setting up monitoring and logging, implementing external security measures, and performing post-deployment validation.

In short, the 5-step version felt more complete and easier to follow because each stage had a clearer purpose. The 3-step plan was good for a quick overview, while the 5-step plan provided a more thorough approach to achieving the goal.

Overall, the agent successfully stayed on track with the given objective. Increasing the number of iterations from three to five made the output more detailed and organized. More steps allowed the agent to think through the process more carefully and produce a more comprehensive plan.