# Intro

This is a work in progress. This coding book was written by me and has not been annotated and summarized by another one at the same time. Therefore, there are many missing issues and other problems. Any feedback and suggestions are welcome! 

Many useful information can be extracted from the Issue discussions on GitHub, including but not limited to: solutions to some problems, reflection of the developers' skills from their discussions. It is reasonable to measure a developer's skills not only from his/her code contributions, but also from his/her discussions with others. 
Undoubtedly, someone's speech reflects his/her personal skill traits.

Skills are not only limited to technical aspects. Especially in Issue discussions, communication abilities, teamwork, problem analysis and problem-solving skills, management abilities, as well as some personal traits such as patience, enthusiasm, initiative, open-mindedness, etc., can all be demonstrated.

Our goal is to extract developers' skills from the discussions, that is, input "developers' words" and output "developers' skills".

This is not an easy task because the information is scattered and fragmented, and the content is about their questions or opinions on a particular issue. We need to infer the underlying skill information from these fragmentary expressions.

To discover the correspondence between "what they said" and "skills", and to reduce the cognitive burden during coding, the author conducted two rounds of coding:

The **first-round** coding was to **classify the contents**:
- First, classify the contents by **issues**, including asking for help, giving advice, problem reporting, new feature reporting, etc.
- Then classify the contents by **sentences**, including communicative language, reference, asking for help, giving help, giving advice, problem reporting, new feature reporting, new feature discussion, problem analysis, problem solving, etc.

The **second-round** coding was to **annotate the skills**:
- Infer their skills based on **sentences, paragraphs, multiple paragraphs, even the entire discussion process of the developer**, including Information Gathering Related, Technical Abilities, Communication Related, Problem Analysis Related, Personality, etc.

# Data

## Scripts

You can crawl the data using the [scripts](https://github.com/YangWenhao3906/Discussions_to_Skills/blob/master/Issues_Scraper.py) in this repo.

**Note**: Please fill in your own GitHub token. You can get it at [https://github.com/settings/tokens](https://github.com/settings/tokens)

This script crawls all closed issues with a discussion number greater than n (set by the user), saves them in JSON format, and uses `\r\n\r\n` to split each message body

## Data you can use to practice

In `/data_practice`, there are issues that have been crawled and processed by the scrip that have not yet been labeled

# Round One of Coding

`example_issue.JSON` is an example by the author. 

## Categories of issue

By reading this issue, put this issue into the following categories. Fill in `issue_categories` field, corresponding to the unit of **paragraph.**

- **problem reporting**: Describing and documenting an issue or problem that has been encountered in order to bring it to the attention of others who can help resolve it.
- **asking for help**: Seeking assistance or guidance from others to address an issue or solve a problem.
- **new feature reporting**: Describing and documenting a request for a new feature or functionality that is not currently available in a system or product.

## Elements of issue discussion

Read each sentence and put it into one of the following categories. Fill in `sentence_categories` and  `comment_categories` field, corresponding to the unit of **sentence** and **paragraph** respectively.

- **communicative language**: Greetings, thanks, apologies, etc
- **reference**: All information is obtained not only from others, but also from oneself, such as when a problem is found in usage.
- **problem reporting**: Describing and documenting an issue or problem that has been encountered in order to bring it to the attention of others who can help resolve it.
- **problem analysis**: Analyze, apply logical reasoning to, or critically think through problems and solutions.
- **problem solving**: Using critical thinking, creativity, and problem-solving skills to develop and implement effective solutions to address an issue or problem.
- **asking for help**: Seeking assistance or guidance from others to address an issue or solve a problem.
- **giving help**: Providing assistance or support to someone who is experiencing an issue or trying to solve a problem.
- **giving advice**: Offering suggestions, recommendations, or guidance on how to address an issue or solve a problem.
- **new feature reporting**: Describing and documenting a request for a new feature or functionality that is not currently available in a system or product.
- **new feature discussion**: Exploring and discussing potential new features or functionality that could be added to a system or product in order to improve its usability or effectiveness.

# Round Two of Coding

Read each sentence. Make the following inference: what skills do I need to possess to say these things? Fill in `sentence_skills`, `issue_skills`, `comment_skills` fields, corresponding to the unit of **sentence** and **paragraph** respectively.

## Skills

- Information Gathering Related
    - Observation: Be able to observe some information keenly
        - Eg: "In DB-Engines Ranking, CrateDB is not in Time Series DBMS category but in Search Engines with ElasticSearch etc."
    - Information Gathering: Able to gather information from a variety of sources
        - Eg: "I studied the classification method of db-engine. For multi-model databases, db-engine sets a primary model for each multi-model database, and the default list is based on the primary model."
        - Eg: "Because GitHub's Events API did not provide events for unstarred activities, it only provided the started type event.\r\n”
- Technical Abilities
    - Language
        - Java, Python...
    - Software Engineering
        - software design
        - software architecture
        - refactoring
        - requirements
    - Domain
        - UI, DB, DL...
    - DevOps: Has knowledge in DevOps to deliver software quickly and efficiently
- Interpersonal Skills
    - Communication: The content is clearly written and easy to understand
    - Collaboration: Works with people from diverse backgrounds to achieve a shared goal
- Problem Analysis Related
    - Analytical: Is able to analyze, apply logical reasoning to, or critically think through problems and solutions
        - Eg: "@hooopo Maybe they dont set their company name in profile ? "
        - Eg: "And should a repo be removed when not actively maintained? Who decides it?”
- Project-Specific Abilities
    - Purpose: Understands and believes in the purpose and societal impacts of the project
        - Eg: "But it can also list in a wider range, including secondary models. OSSInsight's classification is more like the latter, and it may be optimized to be compatible with the two models in the future."
- Personality
    - Initiative: Takes initiative to solve problems and give help
    - Rigor: Demonstrates a commitment to precision, accuracy, and thoroughness
    - Open-minded: Is open to new ideas and viewpoints, and is willing to consider different perspectives and approaches.
    - Creative: Is able to think outside the box and generate innovative solutions to problems.
    - Patient: Is able to remain calm and composed in verbose, difficult or challenging problem, and is willing to take the time needed to discuss and solve it
    - Enthusiasm: Communicates with people with energy, passion, and a positive attitude.

# Our advice

You can ignore this part

We think each element might reflect the following skills:

reference

- Technical skills
- Communication
- Information gathering

problem analysis and solving

- Technical skills
- Communication
- Initiative
- Analytical
- Rigor
- Open-mindedness
- Creativity
- Patience

giving help

- Technical skills
- Communication
- Enthusiasm
- Patience

asking for help

- Communication

bug reporting

- Observation
- Communication

new feature reporting

- Technical skills
- Communication
- Creativity

new feature discussion

- Technical skills
- Communication
- Open-mindedness
- Purpose
