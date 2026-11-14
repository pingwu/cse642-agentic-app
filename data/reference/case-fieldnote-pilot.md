# Case study: Fieldnote pilot with a bakery (fictional)

This case study is fictional sample text for a course exercise. Fieldnote and the bakery do not exist.

## Background

Fieldnote is a pretend start-up that turns a small team's notes into searchable answers. In a four-week pilot it worked with a bakery of nine staff that answers about 60 customer messages a day about orders, allergens and pickup times.

## What was built

The team loaded the bakery's past replies and its allergen sheet into a vector index. A staff member could type a customer's message and see the three closest past replies with their dates.

## Results

- Time to find a past reply fell from about four minutes to under one minute.
- Staff used the tool for 41 of the 60 daily messages by week three.
- Two replies about allergens were found by meaning when the customer used a different word for the same ingredient.

## What went wrong

In week one, an old pickup-time answer ranked first because it matched many words. Adding a filter on the reply date and a source type fixed it. The team also learned to keep each chunk under one allergen topic so that an answer never mixed two products.

## Lesson

Search quality came more from clean chunks and metadata filters than from a bigger model.
