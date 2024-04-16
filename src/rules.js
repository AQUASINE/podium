export const conditionTypes = [
    {
        id: 'none',
        name: 'Always',
        description: "Match all messages.",
    },
    {
        id: 'contains',
        name: 'Contains',
        description: "Match messages that contain a specific string.",
    },
    {
        id: 'exactMatch',
        name: 'Exact Match',
        description: "Match messages that are exactly the same as a specific string.",
    },
    {
        id: 'fuzzyMatch',
        name: 'Fuzzy Match',
        description: "Match messages that are similar to a specific string.",
    },
    {
        id: 'regex',
        name: 'Regex',
        description: "Match messages with a specific regex pattern.",
    },
    {
        id: 'length',
        name: 'Message Length',
        description: "Match messages based on how long they are.",
    },
    {
        id: 'score',
        name: 'Current Message Score',
        description: "Match messages based on the message's current score.",
    },
    {
        id: 'userscore',
        name: 'User Score',
        description: "Match messages based on the user's score.",
    },
    {
        id: 'userblacklist',
        name: 'User Blacklist',
        description: "Match messages from users on a blacklist.",
    },
    {
        id: 'userwhitelist',
        name: 'User Whitelist',
        description: "Match messages from users on a whitelist.",
    },
    {
        id: 'everynth',
        name: 'Every nth Message',
        description: "Match every nth message.",
    },
    {
        id: 'chance',
        name: 'Random Chance',
        description: "Match messages with a certain probability.",
    },
    {
        id: 'seededchance',
        name: 'Seeded Random Chance',
        description: "Match messages with a certain probability based on the message's hash. This means a message will always have the same outcome.",
    },
    {
        id: 'timebased',
        name: 'Time-Based',
        description: "Wait for a certain amount of time before matching a message.",
    }
]

export const actionTypes = [
    {
        id: 'nothing',
        name: 'Do Nothing',
        description: "Simply pass the message through without any modifications.",
    },
    {
        id: 'replace',
        name: 'Simple Replace',
        description: "Replace a specific string with another string.",
    },
    {
        id: 'regex',
        name: 'Regex Replace',
        description: "Replace a string using a regular expression.",
    },
    {
        id: 'drop',
        name: 'Drop Message',
        description: "Drop the message and do not pass it through.",
    },
    {
        id: 'set',
        name: 'Set Score',
        description: "Set the score of the message to a specific value.",
    },
    {
        id: 'math',
        name: 'Math',
        description: "Modify message or user score using math operations.",
        matchingKeywords: ['add', 'subtract', 'multiply', 'divide', 'modulo', 'power', 'root', 'function']
    },
    {
        id: 'add',
        name: 'Add to Score',
        description: "A simple way to add or subtract from the message or user score.",
    },
    {
        id: 'addtag',
        name: 'Add Tag',
        description: "Add a tag to the message or user.",
    },
    {
        id: 'removetag',
        name: 'Remove Tag',
        description: "Remove a tag from the message or user.",
    },
    {
        id: '7tvremove',
        name: 'Remove 7TV emotes',
        description: "Remove 7TV emotes from the message.",
    },
    {
        id: 'gptrank',
        name: 'GPT Rank',
        description: "Use ChatGPT to rank batches of messages based on a prompt.",
    },
    {
        id: 'sentimentAnalysis',
        name: 'Sentiment Analysis',
        description: "Analyze the sentiment of a message.",
    }
]