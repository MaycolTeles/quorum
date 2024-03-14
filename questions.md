1. Q: Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

    A: I used Django as the backend as it is a very powerful framework and it is very easy to use. I used it in a MVT (Model View Template) architecture, so we don't need to create a whole frontend for it. In a scenario with more time, I would use a frontend framework like React or Flutter to make the frontend more dynamic and user-friendly. Also, this way we could use Django in an API form with Django Rest Framework.

    To parse the csv I used Python's default library read the data and then perfom a Bulk create to create all the models. This way the time complexity is O(n) and the effort cost is low.

    Also, since Django provide an admin interface, I used it to make the data visualization and manipulation easier.

---

2. Q: How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or“Co-Sponsors”?

    A: That would be very easy to do, we just need to add the new fields to the model and then add the new fields to the templates to show the data to the user. Also, we would need to change the CSV reader helper to match the new columns, if we're still reading data from the CSV.

    For example, we could add a new field to the `Bill` model like this:
    ```python
    class Bill(models.Model):
        ...
        voted_on_date = models.DateField()
        co_sponsors = models.ManyToManyField(Legislator)
        ...
    ```

---

3. Q: How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

    A: I would create another click command to generate the CSVs. This command could even receive parameters to filter the data, like a specific legislator or bill. Then we would use the `csv` library to create the CSV file and then store it somewhere in the cloud (S3, for example).

---

4. Q: How long did you spend working on the assignment?

    A: Something about 3 to 4 hours, most of the time was spent on the front-end (django templates) to make the pages look good and testing to make sure everything was working as expected.
