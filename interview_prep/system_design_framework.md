# System Design Framework

Use the acronym FAME (Functional Requirements, Analysis, MVP, Expand).

## Functional Requirements

Go over the requirements for the MVP. The interviewer might ask you broadly "how would you design ___?",
in which case, you will need to brainstorm and probe for the requirements. It could be better to list
some of the requirements yourself, and check with the interviewer to ensure you've thought through
the most important aspects.

For each requirement, see if there are follow up questions that should be asked to fine-tune the design.
For instance, if the requirement is that a user should be able to interact with the application, you might
ask what kind of application should the product support - Mobile? Web?

## Analysis

At this stage, you might want to showcase your ability to think through _non-functional requirements_: Security, Scalability, Consistency vs. Availability. Typically,
we would want to estimate some quantitative load on the system which is required to operate:
- Number of active users (ex. Daily Active Users) - e.g., 10 million
- Definition of an active user - e.g., A user that issues 5 searches a day
- Data size, and how much you expect the system to store, transfer, etc. - e.g., 100 Bytes per request 

You can do a rough data estimate, or even QPS.

ex. QPS: 10M Active Users/day * 5 new searches/user * 4 follow-up messages/search = 200M requests / day
ex. Data sizing: 200^6 requests/day * 100 Bytes / request = 2^4 MB / day * 365 days / year = 7.3^6 MB / year ~ 7.3TB/year 

Walk through a few thought processes to help influence choices in the design:
- Is the system going to be read- or write- heavy? 
- Do we care more about consistency or availability?
- How important is latency optimization?

## MVP

The MVP should be implemented with details addressing the following:
- Sketch of the data schema 
- High-level system architecture
- Deeper dive into the API design

Once these components are sketched, step back and demonstrate how the system supports the User Journeys outlined in the functional requirements.

## Expand
- How might the current MVP be scaled to meet the non-functional requirements of the system?
- What are potential faults in the current MVP, and how might they be optimized?
