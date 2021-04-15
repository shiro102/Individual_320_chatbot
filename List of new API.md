# New APIs implementations:
## Wikipedia API
- Whenever the user asks for something that is not in the database, the chatbot looks up for the keyword and search for that keyword in Wikipedia database.
- In the example below, the bot recognizes "CodeGeass" as the keyword and tries searching in wikipedia.
![Wiki](https://media.discordapp.net/attachments/832035518903484458/832035534255423498/unknown.png)
- If there is no page that matches the information that is asked, the bot will say that it cannot find any match.
![Wiki](https://cdn.discordapp.com/attachments/832035518903484458/832052705308311582/unknown.png)

## Google translate API
- Whenever the user asks for something in another language than English, the chatbot automatically translates the sentence to English and processes using the data in the translated sentence. At the end, it translate the reply into the language that the user used. It also apply to the Wiki API. 
- In the example below, the user uses Vietnamese and Chinese as the input, and the bot then replies in the according languages. However, sometimes because the translation is not accurate, the bot will not receive correct translation of the sentence which is demonstrated in the third line of the Chinese-translation image where the bot says that "I dont understand what 'goodbye' is"
![Translate](https://media.discordapp.net/attachments/832035518903484458/832046059094016020/Translate.png?width=1379&height=670)
![Translate2](https://media.discordapp.net/attachments/832035518903484458/832047709531537479/Translate.png?width=1379&height=670)

## Twitter API
- Whenver user inputs a sentence that includes the keyword "twitter" or "tweet", the chatbot will automatically uses Twitter API to look for any tweets that contain the keyword or profile that has the same name as the keyword. The wikipedia and googletranslate APIs will also work with this API.
- In the example below, it searches the twitter of Donald Trump and any tweets that contain the keyword "Donald Trump"
![Translate](https://media.discordapp.net/attachments/832035518903484458/832046059094016020/Translate.png?width=1379&height=670)
- If there is no profile or tweets that match the keyword, the bot will indicate that there is no one or no tweet that matches the keyword.
![Translate](https://media.discordapp.net/attachments/832035518903484458/832053962562994186/unknown.png)
