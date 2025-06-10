{
    "name": "AI Content Agent",
    "description": "Een chatbot die automatisch social media content genereert op basis van doelgroep, platform en tone of voice.",
    "intents": [
        {
            "name": "generate_content",
            "description": "Genereer content op basis van doelgroep, platform en tone of voice.",
            "inputs": [
                {
                    "name": "doelgroep",
                    "type": "string",
                    "required": true,
                    "options": [
                        "Studenten",
                        "Young professionals",
                        "Ouders"
                    ]
                },
                {
                    "name": "platform",
                    "type": "string",
                    "required": true,
                    "options": [
                        "Instagram",
                        "LinkedIn",
                        "TikTok"
                    ]
                },
                {
                    "name": "tone_of_voice",
                    "type": "string",
                    "required": true,
                    "options": [
                        "Informeel",
                        "Professioneel",
                        "Empathisch"
                    ]
                }
            ],
            "responses": [
                {
                    "type": "text",
                    "content": "Hier is de gegenereerde content voor {doelgroep} op {platform} met een {tone_of_voice} tone of voice: {generated_content}"
                }
            ]
        }
    ],
    "actions": [
        {
            "name": "fetch_prompt",
            "description": "Haal de juiste prompt op uit de bibliotheek.",
            "function": "fetch_prompt",
            "parameters": [
                {
                    "name": "doelgroep",
                    "type": "string"
                },
                {
                    "name": "platform",
                    "type": "string"
                },
                {
                    "name": "tone_of_voice",
                    "type": "string"
                }
            ]
        },
        {
            "name": "generate_content",
            "description": "Genereer content met behulp van AI.",
            "function": "generate_content",
            "parameters": [
                {
                    "name": "prompt",
                    "type": "string"
                }
            ]
        }
    ]
}