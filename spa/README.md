# <span style="color: #4361ee">Email Meaningfulness Analyzer SPA

This extremely simple SPA serves as a proof of concept for a Email Meaningfulness Analyzer powered by AI.

# <span style="color: #f72585">Structure

Although it is a simple approach to a simple problem (showing data on the screen), it doesn't mean it can't be modular.

There was no need to segment the code in multiple files, so all of the page is in the `index.html` (excluding the styling, that can be found on the `style.css`).

The page follows a simple card-based structure. It begins with the Welcome Screen card loaded and procceds to load the Main Content and Suggest Section cards as needed. This structure allows the page to be expand in everyway just by adding more cards that fulfill new functions.

The icons are provided by [Font Awesome](https://fontawesome.com/) and the stylesheet was improved by adding some shading on the colors for better reader experience.

## <span style="color: #f7b801">API Connection

There is no need to setup a `.env` for this project, however, when deploying or even running locally, you might want to change the url of the API (around line 190) to your own.

It is the only section of the project that needs this url, so it shouldn't be much trouble. Please don't hesitate in asking for help otherwise.

# <span style="color: #4cc9f0">How can I reach you to get support with this project?

If you need help with this project or to discuss the use of one technology over another, you can email me with:

- arthur-illa@hotmail.com
