from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

## research task
research_task = Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the Channel"
    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} of video content",
    tools=[yt_tool], 
    agent=blog_researcher
)


## Writing task
write_task = Task(
    description=(
        "get the information from the YouTube channel on the topic {topic}"
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog",
    tools=[yt_tool],
    agent=blog_writer,
    async_eecution = False, #both agent will be parallely working if True
    output_file= 'new-blog-post.md'  #o/p file 
)