# MCQ-Langchain-App
A Web application build by Streamlit Python that uses an Integration between Langchain and OpenAI Completion API

### Setting up the environment
- For best practices you need to create a virtual environment you can use any environment you like, but I used virtualenv and created a virutal environment.
- you can do that as well by printing in `cmd` the following command `virtualenv name-the-virtula-env`.
- once done creating the virtual environment you need to install the required packages and libraries to run the code, you can do that in two ways:
  1. manualy using `pip install -the name of the package-`
  2. by using the requirnment.txt file to install all the required packages and libraies by running this command `pip install -r requirements.txt`

Once done with installing all the dependances, now let's discuss the User Interface.
### UserInterface
- The UI is build using Streamlit Pyhton which is a very friendly library that is used to develop web applications for Data Science projects and machine learning with minimal effort.
- The UI for the MCQ applications is pretty simple all you have to do is to enter a topic that you would like to test your knowledge in and select a number of questions to display and interact with and to take the quiz on.
- once you done all of the steps above the quiz will be generated and you can take the quiz and interact with it and after your done and you want to submit your answers all you have to do is to push the submit button
- That will display your score and the correct answer of each question so that you can compare your results with the correct ones (and I added some motivation notes)

Now Let's take about the final part wich is the Functionality
### Functionality
- I used an Integration between Langchain and OpenAI chat model which is OpenAI completion API.
- This Integration works as follows:
  1. First you need to create an openai account.
  2. Then you need to get your API Key and make it as an environment variable so nobody can see it.
  3. Then instantiate the OpenAI Chat model
  4. I created a specifiy prompt template to pass it as a system message to my model so the model can really understand what it should do, and make sure that you pass some kwargs to this prompt like the topic name etc.
  5. after that I parsed the ouput using the Pydentic (Json) parser to get the data output in json format.
  6. finally just feed the system message I created to the model and see the majic.

## Finally
This project is a lot of fun to play around with I would give it a try if I were you
### Links
You can find the code for this project in this link on my github [Visit My Github](https://github.com/Abdulrhman567/MCQ-Langchain-App)
- 
