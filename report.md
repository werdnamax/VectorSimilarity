# Part 5: Reflection Report
Submit reflection report answering the following questions.

## Understanding Vector Databases

1. In your own words, what is a vector embedding?

vector embedding is a way to represent semantic "meaning" of text using a numeric representation which is a multi-dimensional vector or a long "list" of floats representing the text.   

2. How does a vector represent the “meaning” of text?

A vector represents the "meaning" of text by capturing the semantic relationships into high-dimensional space such as 128-1536 dimensions. While each dimension is a bit ambiguous, similar "tokens" of text end up closer together in this space which can be compared mathematically for similarity.     

3. Why is similarity search possible using vectors but not straightforward in traditional relational databases?

With vector a vector database the sematic meaning of the text is encoded into vectors and similar vectors that is text with similar meanings are near each other so you can calculate things that are close. Tradition databases are designed for exact matches or even associations which are predefined using indexes and keys and do not encode any semantic meaning into the text. 

## Comparison to Relational Databases

4. How would you store and query this same data in a traditional relational database?

You would store the data with in rows and columns such as (title, description, code, credit, prerequisites, etc) being columns and then the values within it. You could only query using exact matches or ranges such as classes with credits >= 3, you can do complex queries but they are exact matches [schedule.cs.wallawalla.edu](https://schedule.cs.wallawalla.edu/) is a good example of this.

5. What kinds of queries are relational databases particularly good at?

Relational databases are good at exact match queries such as range queries, joins across related tables, aggregations, and are enforced through constraints. They excel when relationships and queries are well-defined leaving nothing to approximation. 

6. What kinds of queries are vector databases particularly good at?

Vector databases are good at semantic often referred to as "fuzzy" queries because they are not exact matches but rather items which are similar in meaning instead of identical matches.  

7. Why would using SQL alone be insufficient for semantic search?

SQL, using a relational operates on exact values and predefined relationships using simple RegExr comparisons (if even supported). It cannot measure semantic similarity in unstructured text or associate similar concepts only dealing with predefined relationships.      

## MongoDB and Implementation

8. Why is MongoDB a reasonable choice for storing vector data?

MongoDB supports flexible document schemas, making it easy to store vectors and even metadata. While it does apparently provide native similarity search capabilities I decided to make my own using cosine similarities mainly because I could not get it to work.  

9. What challenges did you encounter when storing or querying vectors?

The biggest challenge when it comes to storing data was making sure my functions returned a type which both python could do calculations on and also MongoDB could understand. (I had many errors relating to type coercion and NONE values)

10. What part of the implementation was the most difficult, and why?

Aside from what is mentioned in question 9. I would say the embedding was the most difficult. One of the most challenging aspects was word2vec had a lot of words which were not supported and so it would throw them as NULL (or in python NONE) so I had to strip a lot of the values. Also  

## Applications and Reflection

11. Give one real-world application where vector databases are clearly better than relational databases.

RAG system and more specifically LLMs which break natural language into tokens which are embedded into vectors to calculate the next most likely tokens. LLMs using natural language so they cannot use predefined relationships. 

12. Give one scenario where a relational database would be the better choice.

A relational database would be idea in transactional systems such as a bank and applications which need consistency and also would need to be re

13. How did this assignment change or deepen your understanding of modern databases?

First of all this assignment give me some hands on experience with a real modern database but also deepened my understanding of the inner workings of Vector databases and also a sliver of things like LLMs. 
 