Project Goals:

1. Develop an Agentic pipeline and infrastructure for Migrating Projects from other languages to Rust, while optimizing token/credit consumption, increasing accuracy, enforcing reasoning through agentic pipelines, optimizing context window, and custom skill development for LLM Agents to use. This repository will ultimately become the .agents directory at root dir of its corresponding projects in the future.

2. This repository will ultimately become the .agents directory at root dir of its corresponding projects in the future.

3. This Project must Prevent AI from wasting tokens/credits on producing code or text that will be discarded in the future, and must also prevent duplicated work.

4. to manage context more efficiently, there will be different subagents for different tasks, but only one agent/subagent may work at a time, PARALLEL AGENTS ARE STRICTLY FORBIDDEN.

5. This Project should provide reusable infrastructure for Specification Driven Development via Kani Formal Verification tool, and when appropriate, Bolero with Kani backend: The goal is to turn the domain business logic into Kani Harnesses that describle the expected behavior of the application via the relationship between user input and visible user output. In other words, E2E harnesses. The Kani Harnesses and formal verification tools must NOT be used for technical verification such as testing concurrency, performance, etc. in this phase of development of Project Aegis. Verifying those is postponed to after we can observe domain business logic correctness and direct one to one correspondence between the original project's object model and object/method hierarchy. Once that is achieved, the project will be modified to add those as well. ALL HARNESSES/SPECIFICATIONS MUST BE STRICTLY DERIVED FROM ORIGINAL PROJECT'S TEST SUITE.

6. The Design philosophy of the projects governed by Aegis must be CGP Oriented programming paradigm and design philosophy. The framework CGP will not be merely a utility but will be pervasively used to accelerate development, reduce effort, and decouple different modules of the target project, and make it effortless to easily plug components in and out.

7. There should be precise and STRICT one to one correspondence between the original project's object model, object/method hierarchy and naming conventions. meaning that for each C++/Go/Java/Python class, struct, enum, interface, etc. There will be one object of the same name, with the exception that a combination of a Trait, a struct, an enum and and their methods (Impl blocks) will be considered a single rust object, because in other languages, a class can contain both variables, fields, data, metadata, and functions, and behavioral contracts at the same time, while rust separates them into Traits + Structs + enums and impls. But Aegis must take EXTREMELY STRICT measures to ensure that the LLM Agent does NOT exploit that exception to bypass precise one to one equivalence in Object model, Object/Method/Functionality hierarchy and relationships, and naming conventions.

8. After implementation and verification is fully finished, Documentations will be generated based on CPGSchema, and Based on ISO/IEC/IEEE 42010 Architecture Description.

9. Aegis must provide the capability to create custom skills for the agents. Here is a list of books and documentations which must be ultimately turned into accessible Agent skills that is systematically made available to the Agent effortlessly without agent loosing track of the Project Context, and Skill instructions: Learning Rust with Entirely Too Many Linked Lists, Rust Atomics and Locks, CGP, Kani Book, CGP official docs, Derive deftly official docs, Agones official docs, Bevy Official Docs, Rust book, Rust Reference docs, PyO3 official docs, Bolero official Docs. The books and the docs MUST be turned into skills with ZERO information loss. information loss is NOT tolerated. Here is a list of suggestions for integrating into Aegis for Skills: https://github.com/infiniflow/ragflow.git , https://github.com/deepset-ai/haystack.git , https://github.com/letta-ai/letta-code.git , Zip files containing a large number of suggestions.

10. Maximize Reasoning, and make the possibility of mistakes as close as possible to ZERO MISTAKES. The configuration of Reasoning MUST be set to max by default, and Aegis must enforce it.

11. Aegis must deeply integrate with Codex Goal Plugin and Plan Plugin.

12. Since Aegis is growing larger, it should become more modular and more decoupled, therefore, if necessary, Langgraph + Langchain + Unpythonic must replace raw python code. And for the parts of project implemented in Rust, CGP + Derive Deftly + Arcane Macros ("https://github.com/arcane-rs/arcane") + proc macro 2, proc macro 2 attribute, proc macro 2 derive and proc macro 2 delegate The Rust Frameworks listed in .md files and zip files for Agent Orchestration.

13. In this development cycle, the project will be deeply designed around Developing the projects Carbon Blue and Carbon Destiny and Aegis itself

14. Based on the three prompts for the three projects Aegis, Carbon Blue, and Carbon Destiny, and their reported and documented flaws, Generate three comprehensive Roadmaps. Each roadmap will be stored in its own corresponding directory at root directory. Each Roadmap will be written in a combination of Sequential Markdown files each corresponding to a project milestone, and the markdown files MUST be compiled with Agentic pipeline code that enforces roadmap adherence and reduces thinking and planning effort from the model's side and accelerates development and reduces mistakes, and narrows down project scope, and optimizes token/credit consumption.

15. Only develop in dev branch of the repo, DO NOT MODIFY MAIN. Also, Make stackable pull requests, pushes and merges incrementally to ensure that no progress is duplicated or lost.

16. Analyze all branches of the project to ensure that no progress is duplicated or lost.

17. Use Dagger + GitLab for CI/CD Pipelines to the fullest potential, to accelerate development, deployment, and reduce boilerplate for both Aegis and Carbon Projects.

Target Project Repo: https://github.com/QuasarRay/Aegis.git