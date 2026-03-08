# In-Depth Comparative Analysis of AI Prompt Frameworks

## Table of Contents
1. [The Role of AI Prompts](#the-role-of-ai-prompts)
2. [Overview of Common AI Prompt Frameworks](#overview-of-common-ai-prompt-frameworks)
3. [Analysis of Common AI Prompt Frameworks](#analysis-of-common-ai-prompt-frameworks)
4. [Comparison of All Frameworks](#comparison-of-all-frameworks)
5. [Practical Applications](#practical-applications)
6. [Source Links](#source-links)

---

## The Role of AI Prompts

### Core Value

In the AI era, prompts are the key to communication between humans and large language models (LLMs). People interact with AI models through prompts, and the models work according to these prompts. Only those who master AI prompt engineering methods can better harness artificial intelligence.

Good prompts can:

1. **Clarify Requirements** - Reduce AI's ambiguous interpretation and improve output quality
2. **Guide Reasoning** - Let AI reason according to your way of thinking
3. **Control Style** - Ensure output matches your expected format and style
4. **Improve Efficiency** - Get near-perfect results on the first try, reducing iterations
5. **Lower Costs** - Reduce API calls and token consumption

### Why Structured Prompt Frameworks are Needed

Casual prompts often lead to:
- ❌ **Inconsistent Results** - Different quality answers to the same question
- ❌ **Multiple Iterations Needed** - Extra time and costs
- ❌ **Easy to Miss Important Information** - Output deviates from requirements
- ❌ **Hard to Reuse** - Need to rethink how to express requirements each time

Structured frameworks ensure consistent results through standardized element combinations, allowing you to:
- ✅ Systematically think through requirements
- ✅ Express information completely and clearly
- ✅ Consistently get high-quality output
- ✅ Conveniently reuse and iterate

---

## Overview of Common AI Prompt Frameworks

There are many popular AI prompt frameworks. Here are 7 common ones, each suited for different scenarios:

| Framework | Core Concept | Use Cases | Complexity | Learning Time |
|-----------|-------------|-----------|-----------|-------------|
| **BROKE** | Fast and Direct | Code generation, quick requirements | ⭐ Minimal | 5 min |
| **CRISPE** | Deep Analysis | Problem diagnosis, architecture review | ⭐⭐ Medium | 20 min |
| **ROBOTIC** | Complete Planning | System design, long-term projects | ⭐⭐⭐ Complex | 30 min |
| **Chain-of-Thought** | Step-by-Step Reasoning | Algorithm design, logic verification | ⭐ Minimal | 2 min |
| **CO-STAR** | Creative Output | Content creation, marketing copy | ⭐⭐ Medium | 15 min |
| **ICIO** | Flexible Iteration | Vague problems, gradual optimization | ⭐ Minimal | 10 min |
| **RTF** | Role Play | Scenario simulation, teaching demos | ⭐ Minimal | 5 min |

---

## Analysis of Common AI Prompt Frameworks

### Framework 1: BROKE (Fast Coding Framework)

**What is BROKE**:

- **B**ackground - Project environment and technology stack information
- **R**ole - The role and experience you assign to the AI
- **O**bjective - A clear and specific task to complete
- **K**ey Constraints - Limitations and functional scope during implementation
- **E**xamples - Concrete examples of input/output and structure

**Core Value of BROKE Framework**:

1. **Minimize Ambiguity** - Eliminate confusion through clear constraints and examples
2. **Quick Results** - Suitable for tasks with clear requirements, no need for multiple rounds
3. **Efficient Token Usage** - Concise structure with high information density
4. **Stable Results** - Same BROKE prompt produces consistent output

#### Use Cases

✅ **Best for**:
- Code generation (APIs, functions, configurations)
- Feature implementation (well-designed requirements)
- Quick answers (clear questions)
- Data transformation (format conversion, extraction)

❌ **Not suitable for**:
- System architecture design
- Complex problem analysis
- Creative output
- Tasks requiring multiple review rounds

#### Practical Positive Example

**Scenario**: Generate a login endpoint for a Spring Boot application

```text
[Role]
You are a senior Java architect proficient in Spring Boot 3 and Spring Security, with 10 years of enterprise development experience.

[Background]
Project Environment:
- Spring Boot 3.2 + Java 21
- MyBatis-Plus as ORM
- MySQL 8.0 database
- Using Lombok to simplify code

[Objective]
Implement a complete user authentication system using JWT, including login endpoint, token refresh, and permission verification.

[Key Constraints]
- Password encryption using BCrypt
- Token validity: 24 hours, refresh token validity: 7 days
- Return format: Result<T> unified wrapper
- Include global exception handling
- Follow Alibaba coding standards
- Must use @Slf4j to log critical operations

[Examples]
Input: POST /auth/login
{ "username": "user1", "password": "123456" }

Output:
{
  "code": 200,
  "data": {
    "token": "eyJhbGc...",
    "refreshToken": "eyJ...",
    "expiresIn": 86400,
    "user": { "id": 1, "username": "user1", "roles": ["USER"] }
  },
  "message": "Login successful"
}
```

**Expected Output**: Complete LoginController, AuthService, JWT utility classes, entities and configuration

#### Anti-Example (Bad BROKE Prompt)

```text
[Role]
You are a Java expert

[Background]
I need to make a login feature with Spring Boot

[Objective]
Generate login code for me

[Key Constraints]
- Must be easy to use
- Must be secure

[Examples]
No examples provided
```

**Problems**:
- ❌ Role is vague (what kind of expert?)
- ❌ Background lacks technology stack and version info
- ❌ Constraints too generic ("easy to use" and "secure" are undefined)
- ❌ No specific input/output examples

**Result**: AI will make many assumptions, output may not meet requirements

---

### Framework 2: CRISPE (Deep Analysis Framework)

**What is CRISPE**:

- **C**apacity and Role - Clarify the AI's professional domain and responsibilities
- **R**equest - A clear request statement with specific and concrete topic needs
- **I**nsight - The deeper background of the problem, describing the difficulties encountered
- **S**tatement - Core problem statement, expanding on the "why"
- **P**ersonalization - Tailored to your specific situation
- **E**xperiment - Expected response format

**Core Value of CRISPE Framework**:
1. **Deep Problem Understanding** - Emphasize "why" rather than "what"
2. **Personalized Solutions** - Customized solutions for specific contexts
3. **Transparent Thinking** - See AI's reasoning process
4. **Multi-turn Friendly** - Excellent support for iterative optimization

#### Use Cases

✅ **Best for**:
- Performance problem diagnosis
- Architecture design review
- Complex problem analysis
- Best practice formulation
- Team standards formulation

❌ **Not suitable for**:
- Quick code generation
- Simple one-off questions
- Scenarios requiring immediate action

#### Practical Positive Example

**Scenario**: Diagnose why application response slows down during high concurrency

```text
[Capacity and Role]
You are a senior Java performance optimization expert with 15 years of internet service experience.
You are proficient in: JVM tuning, concurrent programming, Linux system diagnosis, distributed systems.
You do not cover: Database DBA work, front-end performance optimization.

[Request]
Please help me diagnose why my application response slows down during high concurrency and find the root cause.

[Insight]
Our payment system experiences performance issues during evening peak hours:
- Usually P99 response time is 100ms, during peak rises to 5s
- JVM heap utilization 60%, no frequent GC (MaxGCPauseMillis = 200ms)
- CPU utilization 50%, still plenty of CPU resources available
- Database query time is normal (average 10ms), not a database issue
- Logs show many "lock contention" and "park" warnings
- System uses Java 21 + ZGC, deployed on 32-core machine

[Statement]
With sufficient JVM heap, sufficient CPU, and normal database performance,
why does application response still slow down?
Why is performance significantly reduced during peak hours?
What are the most likely causes?

[Personalization]
My technical environment:
- Spring Boot 3.2 with Project Reactor (reactive programming)
- Tomcat thread pool: core=200, max=200, queue=1000
- Local cache: Caffeine (10000 items), secondary cache: Redis
- Dependent services: Payment gateway (average 30ms), inventory service (average 20ms)

[Experiment]
Please answer in the following order:
1. List the 3-5 most likely causes (ranked by probability, explain why)
2. Diagnostic method for each cause (provide specific jstack/jstat commands)
3. Expected performance improvement (percentage)
4. Recommended solution (include code examples)
```

**Expected Output**: Detailed analysis, diagnostic commands, optimized code, performance expectations

#### Anti-Example (Bad CRISPE Prompt)

```text
[Capacity and Role]
You are an expert

[Request]
Help me analyze why the system is slow

[Insight]
The system is slow

[Statement]
How to optimize?

[Personalization]
None

[Experiment]
Give me suggestions
```

**Problems**:
- ❌ Completely insufficient information, AI cannot diagnose
- ❌ No performance data, logs, or technology stack
- ❌ Cannot determine optimization direction

**Result**: Only generic advice possible

---

### Framework 3: ROBOTIC (Complete Planning Framework)

**What is ROBOTIC**:
- **R**ole - Position the AI's professional role and clarify responsibilities
- **O**bjective - Clear final goal, listing specific items
- **B**ackground - Detailed project background, including systems, features, technology stack
- **O**utput - Specific deliverables, clarify what needs to be produced
- **T**ype - Nature of the task, tell AI what kind of task this is
- **I**terate - Plan for multi-round feedback, specify how many rounds
- **C**larify - Questions to eliminate ambiguity beforehand, clarify unclear points

**Core Value of ROBOTIC Framework**:
1. **Completeness** - Full coverage from requirements to deliverables
2. **Iteration Mechanism** - Clear multi-round review and feedback process
3. **Clear Boundaries** - Clarify all assumptions beforehand
4. **Team Collaboration** - Facilitates team communication and review
5. **Long-term Value** - Suitable for projects requiring continuous optimization

#### Use Cases

✅ **Best for**:
- System architecture design
- Microservice migration planning
- Technology selection decisions
- Large feature design
- Team standards formulation
- Tasks requiring multiple review rounds

❌ **Not suitable for**:
- Quick coding tasks
- Simple problems
- Scenarios needing immediate answers

#### Practical Positive Example

**Scenario**: Design an e-commerce order system using DDD

```text
[Role]
You are a senior Java architect with 15 years of internet experience.
Background: Led the architecture design of multiple million-level daily active e-commerce systems
Expertise: DDD domain-driven design, microservice architecture, event-driven design

[Objective]
Task to complete: Use DDD to design aggregate roots and core domain models for e-commerce order services
Final deliverables:
1. Domain model design document (UML class diagram + text explanation)
2. Java implementation code (Order aggregate root, DomainEvent)
3. Business rules document (order state machine, amount validation rules)

[Background]
Project background:
- E-commerce platform, processing 1 million orders daily
- Order lifecycle: Create → Pay → Ship → Receive → Complete/After-sales
- Support multiple payment methods, partial payments, partial shipments, refunds
- Tech stack: Spring Boot 3.2, Java 21, MongoDB (event sourcing)

[Output]
Expected output includes:
1. Mermaid format UML class diagram
2. Java Record/Class implementation (Java 21 features, no setters)
3. Domain event definitions (OrderCreated, OrderPaid, OrderShipped, etc.)
4. Business rules documentation

[Type]
This is an architecture design task requiring:
- Deep domain knowledge modeling
- Rigorous business rule definition
- Consideration of concurrency and consistency issues

[Iterate]
Feedback process:
- Round 1: Core aggregate root and basic state machine
- Round 2: Complete design for partial payments and partial shipments
- Round 3: Concurrency control, event consistency, performance optimization

[Clarify]
Before starting, clarify:
1. Does the order need to support order splitting (1 logical order split into multiple logistics orders)?
2. Do refunds only support original path return, or can they go to other accounts?
3. Use complete event sourcing or hybrid snapshot + event approach?
```

**Expected Result**: Complete architecture solution after 3 rounds of iteration

#### Anti-Example

**Bad ROBOTIC Prompt**:

```text
[Role]
You are an architect

[Objective]
Design order system

[Background]
E-commerce system

[Output]
Code

[Type]
Design

[Iterate]
Multiple rounds of feedback

[Clarify]
No questions
```

**Problems**:
- ❌ All information too concise, AI cannot design
- ❌ No specific business requirements, tech stack, constraints
- ❌ No real clarification questions

---

### Framework 4: Chain-of-Thought (Step-by-Step Reasoning Framework)

**What is Chain-of-Thought (CoT)**:

Require the AI to **show the reasoning process step-by-step** rather than giving direct answers. This is an enhancement framework that can be combined with other frameworks.

**Core Value of Chain-of-Thought**:

1. **Improve Accuracy** - Research shows CoT significantly improves correctness on complex tasks
2. **Process Transparency** - Can verify the logic of each step
3. **Facilitate Learning** - AI's thinking becomes your learning material
4. **Easy to Debug** - Can see which step went wrong when you don't understand the answer
5. **Strong Composability** - Can be combined with any framework

#### Use Cases

✅ **Best for**:
- Algorithm design and analysis
- Logic reasoning and argumentation
- Mathematical problem solving
- Architecture decision verification
- Problem diagnosis and analysis

❌ **Not suitable for**:
- Simple problems (becomes unnecessarily verbose)
- Scenarios requiring quick answers

#### Practical Positive Example

**Scenario**: Analyze and optimize inefficient database query code

```text
You are a senior database performance optimization expert.

Problem: Why is the following code slow when processing 1 million data records? How should it be optimized?

Code:
List<User> users = database.queryAllUsers(); // 1 million records
List<String> activeEmails = new ArrayList<>();
for (User user : users) {
    if (user.isActive() && user.getEmail() != null) {
        activeEmails.add(user.getEmail());
    }
}

Requirement: Please analyze and answer step-by-step following these steps:
1. Analyze the problem: Identify performance bottlenecks in the code
2. Evaluate costs: Calculate time complexity and memory cost of current approach
3. List options: Propose 2-3 different optimization approaches
4. Compare approaches: Compare pros and cons of each approach
5. Recommend approach: Give the optimal approach and implementation code
6. Performance expectations: Predict performance improvement percentage after optimization

Finally, give a summary answer.
```

**Expected Result**:

- AI will step-by-step analyze bottlenecks (full load + application layer filtering)
- Point out time and space costs
- Suggest SQL optimization, Stream optimization, etc.
- Provide complete code and performance comparison

#### Anti-Example

**Bad Chain-of-Thought usage**:

```text
Simple question: What is a getter method?

Requirement: Please think step-by-step and show complete reasoning process.
```

**Problems**:
- ❌ Overusing CoT on simple problems
- ❌ Creates unnecessary verbose responses
- ❌ Wastes tokens

---

### Framework 5: CO-STAR (Creative Content Framework)

**What is CO-STAR**:
- **C**ontext (Background) - Background information about product/service
- **O**bjective (Goal) - Clear marketing objective
- **S**tyle (Style) - Visual and language style of creation
- **T**one (Tone) - Overall tone and emotion
- **A**udience (Target Audience) - Description of target people
- **R**esponse Format (Response Format) - Output format and length

**Core Value of CO-STAR Framework**:
1. **Style Highly Controllable** - Style and Tone make output match requirements
2. **Clear Target Audience** - Content for specific audiences is more effective
3. **Easy to Adjust** - Change style for rapid iteration
4. **Consistent Results** - Multiple versions stay stylistically aligned
5. **Non-technical Friendly** - Not just for programmers, marketing teams can use it too

#### Use Cases

✅ **Best for**:
- Product launch copy
- Marketing emails
- Brand stories
- Advertising ideas
- Social media content
- Any content creation requiring style control

❌ **Not suitable for**:
- Code generation
- Technical documentation
- Pure logic reasoning

#### Practical Positive Example

**Scenario**: Create social media copy for new product launch

```text
[Context]
We developed a new open-source Java framework "FastAPI"
for quickly building high-performance REST APIs.
Core advantages: Simple configuration, fast startup (500ms), gentle learning curve.
Competitors: Spring Boot (full-featured but complex configuration).

[Objective]
Attract young Java developers to try it and gain GitHub Star growth.
Expected results: Tweet likes > 50, shares > 20.

[Style]
Reference copy style of open-source projects like TensorFlow, Vue.js.
Characteristics: Concise and powerful, highlight advantages without disparaging competitors, include code examples.

[Tone]
Overall tone: Friendly, enthusiastic, confident.
Avoid: Overhyping, complex jargon, boring.

[Audience]
Target people: Java developers with 1-10 years of experience.
They care about: Development efficiency, code conciseness, learning costs.
Pain points: Spring Boot complex configuration, long framework learning time.

[Response Format]
Output 3 versions:
1. Twitter copy (within 280 characters, include #hashtags)
2. Tech blog summary (200-300 characters, highlight core advantages)
3. GitHub README "Why choose FastAPI" section (500 characters)
```

**Expected Result**: Attractive social media copy, blog summary, GitHub copy

#### Anti-Example

**Bad CO-STAR Prompt**:

```text
[Context]
New product FastAPI

[Objective]
Write copy

[Style]
Good looking

[Tone]
Good

[Audience]
Developers

[Response Format]
Copy
```

**Problems**:
- ❌ "Good looking" style too vague
- ❌ "Good" tone not specific
- ❌ "Developers" audience too broad (what kind of developers?)
- ❌ No format requirements

---

### Framework 6: ICIO (Flexible Iteration Framework)

**What is ICIO**:
- **I**nit (Initialize) - Propose initial problem and idea
- **C**larify (Clarify) - Round 1 clarification of key information
- **I**terate (Iterate) - Rounds 2-N iterative optimization
- **O**utcome (Outcome) - Final solution synthesizing multiple rounds

**Core Value of ICIO Framework**:

1. **Flexible Iteration** - Not fixed rounds, adjust based on needs
2. **Progressive Refinement** - From vague to clear, from simple to complex
3. **Efficient Feedback** - Quickly validate idea feasibility
4. **Divergence then Convergence** - First explore multiple directions, then focus on optimal
5. **Problem Adaptive** - Especially suitable for scenarios with unclear initial requirements

#### Use Cases

✅ **Best for**:
- Problems with unclear requirements
- Gradual optimization tasks
- API design iteration
- Architecture solution evolution
- Performance optimization diagnosis

❌ **Not suitable for**:
- Scenarios needing quick answers
- Simple clear problems
- Real-time emergency situations

#### Practical Positive Example

**Scenario**: Design a user query API that requires gradual optimization

```text
[Init]
Initialize problem:
Design a REST API for querying user list
Initial idea: GET /users returns all users

[Clarify - Round 1]
I need to clarify the following information:
1. How many users? Do we need pagination?
2. Do we need filtering (by status, department, permissions, etc.)?
3. Do different clients need different fields?
4. What are the performance requirements (P99 latency target)?
5. What is the estimated concurrency (QPS)?

Based on your answer, I will provide an improved API design.

---

Assume your answer is:
- 1 million users, pagination needed
- Need to filter by department and status
- Different clients need different fields
- Performance requirement P99 < 200ms

[Iterate - Round 2]
Based on your requirements, my improved approach:
1. Add pagination parameters: page, pageSize
2. Add filtering parameters: department, status
3. Add field selection: fields parameter or use GraphQL

Now the question is:
- Should field selection use fields parameter or GraphQL? Why?

[Iterate - Round 3]
Based on your choice, the final approach includes:
1. Complete API design (path, parameters, response)
2. Caching strategy recommendations
3. Database index recommendations
```

**Expected Result**: Optimal API design after multiple iterations

#### Anti-Example

**Bad ICIO Prompt**:

```text
[Init]
Help me design an API

[Clarify]
(No specific questions)

[Iterate]
(No feedback provided)

[Outcome]
Give me the final solution
```

**Problems**:
- ❌ Initial problem too vague
- ❌ Clarify stage has no specific questions
- ❌ Iterate process has no feedback

---

### Framework 7: RTF (Role-Playing Framework)

**What is RTF**:
- **R**ole (Role) - Assign the AI a specific role
- **T**ask (Task) - Specific task under this role
- **F**ormat (Format) - Expected output format and style

**Core Value of RTF Framework**:
1. **Role Reinforcement** - Clear Role significantly changes AI's response style and depth
2. **Realistic Scenario** - Simulating real scenarios gets more realistic answers
3. **Ultra Simple and Efficient** - Only 3 elements, lowest learning cost
4. **Easy to Combine** - Can be combined with other frameworks
5. **Teaching Friendly** - Can simulate various roles for teaching

#### Use Cases

✅ **Best for**:
- Technical interview practice
- Student and teacher role-playing
- Product manager discussions
- Role-specific consulting
- Scenario simulation

❌ **Not suitable for**:
- Code generation (while possible, BROKE is better)
- Tasks requiring explicit constraints

#### Practical Positive Example

**Scenario**: Simulate Google technical interview

```text
[Role]
You are a senior technical interviewer at Google
Background: 10 years of interview experience, interviewed 500+ candidates
Characteristics: Friendly but strict, will dig deeper based on answers, ask leading questions
Expertise: Algorithm ability, system design, programming practices

[Task]
Conduct a mock algorithm interview for me
Difficulty: Medium (LeetCode difficulty)
Duration: 45 minutes
Expected evaluation points: Data structures, time complexity analysis, code quality

[Format]
Please follow this process:
1. Present an algorithm problem with complete problem description
2. Listen to my approach and implementation, give feedback
3. If I get stuck, give hints rather than direct answers
4. Let me write code (pseudocode or real code both fine)
5. Review code quality (naming, logic, edge cases)
6. Discuss time and space complexity
7. Finally give comprehensive evaluation and improvement suggestions
```

**Expected Result**: Realistic interview experience

#### Anti-Example

**Bad RTF Prompt**:

```text
[Role]
Interviewer

[Task]
Interview

[Format]
Conversation
```

**Problems**:
- ❌ Role too vague (what company? what style?)
- ❌ Task not specific (what difficulty? how long?)
- ❌ Format has no specific steps

---

## AI Prompt Framework Comparison

### Dimension Comparison Table

| Dimension | BROKE | CRISPE | ROBOTIC | CoT | CO-STAR | ICIO | RTF |
|-----------|-------|--------|---------|-----|---------|------|-----|
| **Learning Cost** | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐ | ⭐ |
| **Number of Elements** | 5 | 6 | 7 | 1 | 6 | 4 | 3 |
| **Suitable for Code Generation** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Suitable for Content Creation** | ❌ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Suitable for Architecture Design** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ❌ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Iteration Friendliness** | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **First-Time Success Rate** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Completion Time** | Fast | Medium | Slow | Fast | Medium | Slow | Fast |
| **Suitable for Team Collaboration** | Weak | Medium | Strong | Weak | Medium | Strong | Medium |

### Framework Selection Decision Tree

```
What is the problem type?
├─ Code Generation
│  ├─ Clear requirements? → BROKE (recommended) / RTF
│  └─ Multiple review rounds needed? → ROBOTIC
│
├─ Content Creation
│  ├─ Style control needed? → CO-STAR (recommended)
│  └─ Gradual optimization needed? → ICIO / CO-STAR
│
├─ Problem Analysis
│  ├─ Deep understanding needed? → CRISPE (recommended)
│  └─ Step-by-step diagnosis needed? → ICIO
│
├─ Architecture Design
│  ├─ Multiple review rounds needed? → ROBOTIC (recommended)
│  ├─ Quick iteration needed? → ICIO
│  └─ Deep analysis needed? → CRISPE + ROBOTIC
│
├─ Logic Reasoning
│  └─ Show process? → Chain-of-Thought (recommended)
│
└─ Role-Playing
   └─ RTF (recommended)
```

### Framework Combination Strategy

Different frameworks can be combined for stronger effects:

**1. BROKE + Chain-of-Thought**
- Used for: Complex code generation, need to show design thinking
- Advantages: Has both code directness and reasoning transparency

**2. CRISPE + Chain-of-Thought**
- Used for: Problem diagnosis, need complete reasoning process
- Advantages: Has both deep analysis and step-by-step reasoning

**3. ROBOTIC + ICIO**
- Used for: Long-term project iterative planning
- Advantages: Has both complete planning and flexible iteration

**4. CO-STAR + Chain-of-Thought**
- Used for: Creative content creation, need to show creative sources
- Advantages: Has both style control and creative process transparency

**5. RTF + BROKE**
- Used for: Role-specific code generation
- Advantages: Has both role reinforcement and code directness

---

## Practical Applications

### Practical Case 1: Quickly Generate Microservice Health Check Endpoint

**Scenario**: Building a microservice architecture and need to quickly implement health check endpoints for all services.

**Choose Framework**: BROKE

**Prompt**:

```text
[Role]
You are a senior Java architect proficient in Spring Boot 3 and microservice architecture, with 12 years of enterprise development experience.

[Background]
Project environment:
- Spring Boot 3.2 + Java 21
- Using Spring Cloud and Consul as service registry
- Need to integrate Micrometer for performance monitoring
- Deployed on Kubernetes, container health checks depend on this endpoint

[Objective]
Implement a standard microservice health check interface supporting Consul health check and Kubernetes readiness/liveness probes.

[Key Constraints]
- Should implement Spring's HealthIndicator interface
- Check items include: database connection, Redis connection, dependent service availability
- Response format must comply with Spring Boot specification
- Health check endpoint should be lightweight, response time < 100ms
- Should set status to STARTING on service startup (upgrade to UP within 30 seconds)
- Detailed logging of each check item result

[Examples]
Input: GET /actuator/health
Output example:
{
  "status": "UP",
  "components": {
    "db": { "status": "UP", "details": { "database": "MySQL" } },
    "redis": { "status": "UP", "details": { "version": "7.0" } },
    "paymentService": { "status": "UP", "details": { "responseTime": "25ms" } }
  },
  "timestamp": "2024-03-07T10:00:00Z"
}
```

**Expected Output**: Complete HealthIndicator implementation, configuration classes, test cases

---

### Practical Case 2: Diagnose Data Consistency Issues in Distributed Systems

**Scenario**: Order system shows data inconsistency during high concurrency, need to diagnose root cause.

**Choose Framework**: CRISPE + Chain-of-Thought

**Prompt**:

```text
[Capacity and Role]
You are a senior distributed systems expert with 15 years of internet service experience.
You are proficient in: Distributed transactions, message queues, data consistency patterns, concurrency control.

[Request]
Please help me diagnose why my order system has data inconsistency during high concurrency and find the root cause and solution.

[Insight]
Problems we encountered:
- When users place orders, order table shows "paid", but inventory table still shows not deducted
- This causes the same item to be purchased by multiple users, exceeding inventory
- Problem occurs during peak hours (QPS > 1000), normal during off-peak
- We used local @Transactional but no distributed transactions across services
- System architecture: OrderService → PaymentService → InventoryService
- Currently using synchronous RPC calls (no retry mechanism)

[Statement]
Core question: In what concurrency scenario does this problem occur? What is the root cause?

[Personalization]
My technical environment:
- Spring Boot 3.2, MySQL 8.0
- Payment service call time: 50-200ms (unstable)
- Inventory deduction is synchronous call, no circuit breaker
- Not using message queue or Saga pattern
- Team has 8 people, 2 years microservice experience

[Experiment]
Please analyze in the following order:
1. **Step 1**: Draw a sequence diagram for concurrency scenarios, explain how the problem occurs
2. **Step 2**: Analyze shortcomings of current architecture (synchronous calls, lack of isolation, etc.)
3. **Step 3**: List 3-5 possible solutions (ranked by priority)
4. **Step 4**: Based on my team size and experience, recommend best solution and implementation plan
5. **Step 5**: Give improved pseudocode showing how to handle various failure scenarios

Finally, summarize the root cause in one sentence.
```

**Expected Output**: Sequence diagram, problem analysis, 3 solutions, recommended approach, improved code

---

### Practical Case 3: Design a Complete Microservice System Architecture and Plan Migration

**Scenario**: Company migrating from monolithic to microservice architecture, need complete architecture design and migration plan.

**Choose Framework**: ROBOTIC + ICIO

**First Phase Prompt (ROBOTIC Draft)**:

```text
[Role]
You are a senior tech lead and microservice architect
Background: Successfully led 3 major system refactoring from monolith to microservices
Expertise: Microservice decomposition strategy, distributed transactions, team coordination, risk management

[Objective]
Task to complete: Develop complete microservice architecture design and migration plan for existing monolithic application
Final deliverables:
1. Architecture evolution roadmap (phased, timeline)
2. Microservice decomposition design (service boundaries, data models, communication methods)
3. Implementation plan and risk assessment

[Background]
Project background:
- Existing monolithic Java application, 800,000 lines of code, running for 8 years
- Process 50 million requests daily, P99 response time 300ms
- Core modules: Orders, Payments, Inventory, Logistics, After-sales
- Tech stack: Java 8 + Spring MVC + MySQL, single machine deployment
- Team size: 30 people (15 backend)
- Migration expectation: 6-12 months, no service interruption

[Output]
Expected output includes:
1. Microservice decomposition approach (include Mermaid architecture diagram)
2. Service communication design (sync/async, protocol selection)
3. Data consistency approach (distributed transactions, Saga, etc.)
4. Phased migration plan (deliverables and test plan for each phase)
5. Risk assessment and mitigation measures

[Type]
This is a strategic architecture design and planning task, requiring balance between:
- Technical ideals vs real constraints
- One-time migration vs gradual migration
- Team capability vs technical complexity

[Iterate]
Feedback process:
- Round 1: Initial microservice decomposition and overall timeline
- Round 2: Optimize decomposition boundaries and communication methods based on team feedback
- Round 3: Refine specific implementation steps and risk mitigation for each phase

[Clarify]
Before starting, clarify:
1. How many people on the team have microservice experience? Do they need skills upgrade?
2. Team acceptance of new technologies (like Kafka, gRPC)?
3. Data consistency requirements (strong consistency vs eventual consistency)?
4. Existing DevOps infrastructure (Docker, K8s)?
5. Critical business constraints during migration (SLA, maintenance windows, etc.)?
```

**Iteration After Round 1 (ICIO Style)**:

```
User feedback: "Our team mainly has monolithic experience, microservices not much. We have K8s infrastructure but limited Kafka experience. Data consistency needs to support eventual consistency only."

[Iterate - Round 2]
Based on your feedback, my adjusted approach:
1. Prioritize simpler service decomposition (split 3-4 core services first)
2. Communication approach: Prioritize synchronous RPC (Spring Cloud + Feign), introduce message queue in phase 2
3. Distributed transactions use Saga pattern, but initially implement programmatically, consider frameworks later
4. Schedule 2 weeks of team training in phase 1 (microservice fundamentals, Feign, distributed transactions)

Now the question is:
- In these constraints, which 3-4 services should we prioritize splitting?
```

**Expected Result**: Complete migration plan after 2-3 iterations

---

## Source Links

All framework detailed documentation and example code can be found at:

### Complete Framework Documentation
- 📄 [BROKE Framework Guide](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks/BROKE.md) - Fast Coding Framework
- 📄 [CRISPE Framework Guide](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks/CRISPE.md) - Deep Analysis Framework
- 📄 [ROBOTIC Framework Guide](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks/ROBOTIC.md) - Complete Planning Framework
- 📄 [Chain-of-Thought Framework Guide](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks/Chain-of-Thought.md) - Step-by-Step Reasoning Framework
- 📄 [CO-STAR Framework Guide](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks/CO-STAR.md) - Creative Content Framework
- 📄 [ICIO Framework Guide](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks/ICIO.md) - Flexible Iteration Framework
- 📄 [RTF Framework Guide](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks/RTF.md) - Role-Playing Framework

### Related Resources
- 📚 [AI Programming Prompt Engineering Complete Guide](https://github.com/microwind/ai-prompt/blob/main/programmer_prompt_engineering_guide.md) - AI Programming Prompt Best Practices
- 📚 [Vibe Coding Prompt Engineering Guide](https://github.com/microwind/ai-prompt/blob/main/developer_prompt_engineering_guide.md) - Vibe Coding Prompt Best Practices
- 🎯 [100+ Prompt Examples](https://github.com/microwind/ai-prompt/blob/main/Prompt-Frameworks) - Practical Application Examples for Various Scenarios

---

## Summary and Best Practices

### Golden Rules for Framework Selection

1. **BROKE** - When your problem is clear, requirements are explicit, and you need code
2. **CRISPE** - When you need deep analysis, problem diagnosis, and understanding causes
3. **ROBOTIC** - When you want to design systems, need multiple review rounds, involve team collaboration
4. **Chain-of-Thought** - When you need to see reasoning process, verify logic (can combine with other frameworks)
5. **CO-STAR** - When you want to create content, control style, clarify audience
6. **ICIO** - When problem is unclear, need gradual optimization, need multiple rounds of feedback
7. **RTF** - When you want role-playing, simulate scenarios

### 5 Key Points to Improve Prompt Quality

1. **Specific rather than vague**
   - ❌ "Write login in Java"
   - ✅ "Use Spring Boot 3.2, JWT, BCrypt, return Result<T> format"

2. **Complete rather than fragmented**
   - ❌ Only describe output format
   - ✅ Describe background, constraints, and provide input/output examples

3. **Clear rather than ambiguous**
   - ❌ "Code should be good"
   - ✅ "Follow Alibaba coding standards, include Javadoc, complete exception handling"

4. **With examples rather than without**
   - ❌ Only describe requirements
   - ✅ Provide concrete input/output examples

5. **Verifiable rather than vague**
   - ❌ "Performance will be very fast"
   - ✅ "Performance improvement 50% or more"

### When to Combine Frameworks

When a single framework cannot meet requirements, consider combining:

- **BROKE + Chain-of-Thought** = Code generation with thinking
- **CRISPE + Chain-of-Thought** = Verifiable problem diagnosis
- **ROBOTIC + ICIO** = Flexible long-term planning
- **CO-STAR + Chain-of-Thought** = Creative content generation

---

**Finally**:

Choosing the right prompt framework is like choosing the right development tool. Good tools significantly improve efficiency. The most important thing for leveraging AI programming is expressing requirements clearly, converting business needs into explicit technical requirements, and telling the AI **what you want**—express requirements clearly, provide complete information, and clear constraints. Master these frameworks and you can collaborate with AI more efficiently.

### Source Links
[https://github.com/microwind/ai-prompt](https://github.com/microwind/ai-prompt)