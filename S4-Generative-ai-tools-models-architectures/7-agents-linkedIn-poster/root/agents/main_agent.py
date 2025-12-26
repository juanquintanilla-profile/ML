from specialized_agents import ( 
    MarkingAgent,
    ProgrammingAgent,
    LegalAgent
)

class MainAgent:
    def __init__(self):
        self.marketing = MarkingAgent()
        self.programing = ProgrammingAgent()
        self.legal = LegalAgent()

    