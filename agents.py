from crewai import Agent 
from tools import yt_tool
from langchain_groq import ChatGroq

## create a senior blog content researcher
llm = ChatGroq(
            groq_api_key="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",
            model_name='mixtral-8x7b-32768'
    )

blog_researcher = Agent(
    role= 'Blog researcher for Youtube Videos',
    goal= 'get the relevant video transcript fro the topic {topic} from YouTube channel',
    verbose= True,
    memory= True,
    backstory= (
        "Expert in understanding videos in AI DataScience, Machine Learning and GEN AI and providing suggestion"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
    # name= ''
    # description= ''
)

## creating a senior blog writer agent with YT tool

blog_writer = Agent(
    role= 'Blog writer',
    goal= 'Narrate Compelling tech stories about the video {topic} from YT channel',
    verbose= True,
    memory= True,
    backstory= (
        "With a flair of simplifying comple topics, you craft"
        "engaging narratives  that captivate and educate, brigning new"
        "discoveries to light in an accessible manner"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
    # name= ''
    # description= ''
)