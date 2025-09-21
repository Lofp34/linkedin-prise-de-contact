# LinkedIn Prise de Contact - CrewAI

Projet de prise de contact automatisée sur LinkedIn utilisant [crewAI](https://crewai.com). Ce système utilise des agents IA collaboratifs pour analyser les profils LinkedIn et générer des messages de prise de contact personnalisés.

## Installation

### Prérequis
- Python >=3.10 <3.14
- Node.js (pour les outils MCP HDW)

### Installation rapide avec pip

1. Clonez le repository :
```bash
git clone https://github.com/Lofp34/linkedin-prise-de-contact.git
cd linkedin-prise-de-contact
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez les variables d'environnement :
```bash
cp .env.example .env
# Éditez le fichier .env avec vos clés API
```

### Installation avec UV (recommandé)

1. Installez UV si ce n'est pas déjà fait :
```bash
pip install uv
```

2. Installez les dépendances :
```bash
uv pip install -r requirements.txt
```

Ou utilisez la commande CrewAI :
```bash
crewai install
```

### Configuration

**Configurez vos clés API dans le fichier `.env` :**

- `OPENAI_API_KEY` : Votre clé API OpenAI (requis)
- `HDW_ACCESS_TOKEN` : Token d'accès Horizon Data Wave (requis)
- `HDW_ACCOUNT_ID` : ID de votre compte HDW (requis)

### Personnalisation

- Modifiez `src/hdw/config/agents.yaml` pour définir vos agents
- Modifiez `src/hdw/config/tasks.yaml` pour définir vos tâches
- Modifiez `src/hdw/crew.py` pour ajouter votre logique, outils et arguments spécifiques
- Modifiez `src/hdw/main.py` pour ajouter des entrées personnalisées pour vos agents et tâches

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the hdw Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The hdw Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Hdw Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
