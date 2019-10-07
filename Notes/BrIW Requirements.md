BrIW Requirements

This list of requirements applies to the BrIW web frontend and API, not the command-line interface.

- As a user, I want to add new drinks and people to the app so that I can keep the app up-to-date, in case people leave or join the team, or new drinks are available
- As a user, I want to be able to store the favourite drink of everyone in my team, so I know what to get them when they ask for a drink.
- As a brewer person I want to be able to create a brew round so my teammates can submit brew requests so that I know who wants a drink. The application should know what drink they want based on their preferences
- As a person setting up the round I want to be able to assign a “Brewer” to the round so that people know who is making the drinks
- As a user I want to be able to enter the name of the people in my team that want a drink so that I can get a list of all the people who want a drink and what the drinks are
- Write a unit test suite for your application.
- Write an integration test suite for your application
- Write a README document for your application containing;
  - What the application is
  - The setup required to run the application
  - How to run the application
  - How to contribute to it
- Modify your application so it is able to save people, drinks and preferences out to a database
- Create static marketing page for BrIW
- Web page generated through application showing current round info
- Create two API endpoints for your application
  - GET: get information about the current round (if there is one) so that people know if they can submit brew requests
    - Show the name of the person running that round
    - Display a list of the current brew orders
  - POST: submit a new brew request to an open round
    - The user will submit their name and either;
      - Use the preferred drink saved in the database
      - Or use a supplied drink in the request
    - Return a success status code if the user’s order was entered successfully in the round
  - JSON is the preferred message encoding format for these endpoints
- Create a website for BrIW in which users can
  - View details of the current round
    - Show the name of the person running that round
    - Display a list of the current brew orders
  - Submit brew orders if there is an active round
    - A form should be displayed prompting the user to enter their name in order to submit their order
    - The drink to add to the order will come from;
      - Preferred drink stored in the database for the user
      - Or supplied on the form