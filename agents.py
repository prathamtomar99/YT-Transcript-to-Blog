from crewai import Agent 

## create a senior blog content researcher

blog_researcher = Agent(
    role= 'Blog researcher for Youtube Videos',
    goal= 'get the relevant video transcript fro the topic {topic} from YouTube channel',
    verbose= True,
    memory= True,
    backstory= (
        "Expert in understanding videos in AI DataScience, Machine Learning and GEN AI and providing suggestion"
    ),
    tool=[],
    allow_delegation=True
    # name= ''
    # description= ''
)

## creating a senior blog writer agent with YT tool
