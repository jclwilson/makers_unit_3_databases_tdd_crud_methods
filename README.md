# Designing repository class "create" and "delete" methods

Keywords: Python, Test-Driven Design, Postgres, Object Oriented Design.

This took some time, but I'm happy with the result.

I made things significantly harder for myself by creating a timestamp columns for post publication date and for user signup date, furthermore, these dates are handled by the database itself. I spent some time trying to implement mocks and patches, before seeking advice from a tutor, who explained that in this case, mocking and patches would not be necessary, rather that I only had to check against the values I'd submitted.
