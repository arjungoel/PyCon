* `GraphQL` is a Query Language for your API where you provide certain fields in the API and get exactly what you have asked for in response.
    - It has some Specification, implemented in many languages and frameworks.
    - Provides a system of constraints that helps us drive a constantly evolving API.



## AGENDA:


- What is GraphQL and what are its benefits?
- How do I get started with GraphQL in python?
- What does it mean for an API to be Relay-compliant?
- What kinds of changes are safe to make to my API as clients being consuming it?
- How can I ensure my GraphQL API performs well?
- How should I design mutation responses for my GraphQL API to serve client needs?



Ques: Why GraphQL?
- GraphQL asks for what you need and get exactly that.
- It avoids data over-fetching by clients.
- It makes easy for clients to express field-by-field data requirements, lazily evaluated on server.
- Encourages concentration of business logic and domain model in API and backend.
- Keep clients lean, focused on presentation of data.
- Easier to pivot or add a new platform in the future.
- There is one request for all your data needs. This means we can avoid `N+1` requests for resources in clients.
- Most data can be fetched on page load in one request or catered to specific components or user interactions.
- Single endpoint increases discoverability and avoids versioning more endpoints.
- It also describes what is possible with a type system.


> Note: Everything in GraphQL is `statically typed`, the specification requires a schema with every field `defined` and `typed`.

- We can introspect our GraphQL schema in real-time provided documentation and powerful tooling and its also a contract with clients. Clients themselves actually requests the data using static
queries against the static schema ensuring that we have a safe contract and that's something we can use to validate for breaking changes in our API.
- We can also evolve our API without versions so GraphQL schema provides a safe guide for evolving over time.
- It also provides first class tools for deprecation and controlled changes to APIs in case we can't evolve safely.


> Static schema typing and runtime introspection enables tooling to help you move faster. (for e.g.- IDE-like editors for rapid prototyping of queries for clients and clients like `graphiql`).

- We can also have robust clients in our front-end web applications to manage concerns like caching and asynchronous actions which lets you focus on code that matters. (for e.g. `Apollo`)

`graphene` is a fully featured client or a server. There are other options like `Ariadne` and `Strawberry`.

- GraphQL is used in unifying API for any kind of data source which means we can leverage that as glue for other data sources and APIs because it has that static type it is easy to provide 
that back-end for microserves of our data-sources.



## LECTURES + Exercises:
    
    # GraphQL + Graphene basics
    # Relay Compliance
    # Schema Evolution
    # Performance
    # Mutations + Client side concerns



## COMMANDS TO BE USED:


### To setup dependencies (`pipenv`, `graphene`, `django` etc.) and fixture data (sqlite) using `invoke` --> `pip install invoke`
### Check setup - lint and test code --> `invoke check`
### Start Django Server --> `invoke start`
### Open GraphiQL in your web browser --> `xdg-open http://localhost:8000/graphql`
