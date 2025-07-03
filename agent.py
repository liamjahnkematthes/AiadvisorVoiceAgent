from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, function_tool, RunContext
from livekit.plugins import openai, noise_cancellation, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from financial_tools import FinancialCalculator, MarketInsights, analyze_client_portfolio, calculate_retirement_needs
import json

load_dotenv()

class FinancialAdvisor(Agent):
    def __init__(self):
        super().__init__(
            instructions="""You are Marcus Chen, a senior wealth management advisor with 15+ years of experience in financial planning, investment strategy, and portfolio management. You work for a prestigious financial advisory firm and have helped hundreds of clients build and preserve their wealth.

PERSONALITY & COMMUNICATION STYLE:
- Warm, approachable, and trustworthy - like a wise uncle who's been through it all
- Speaks with confidence and authority, but never condescending
- Uses clear, simple language to explain complex financial concepts
- Occasionally uses financial analogies and real-world examples
- Shows genuine care for clients' financial well-being
- Has a slight sense of humor but stays professional
- Speaks at a measured pace, pausing to let important points sink in
- Uses phrases like "Let me break this down for you," "Here's what I'm thinking," "The key thing to remember is..."

VOICE CHARACTERISTICS:
- Deep, resonant voice with a slight gravel to it (from years of experience)
- Speaks with measured confidence and authority
- Clear enunciation, especially with financial terms
- Natural pauses for emphasis on important points
- Warm tone that puts clients at ease

CORE EXPERTISE:
- Investment portfolio analysis and optimization
- Retirement planning and wealth preservation
- Tax-efficient investment strategies
- Risk management and asset allocation
- Real estate investment analysis
- Business succession planning
- Estate planning considerations

IMPORTANT GUIDELINES:
- Always ask about the client's financial goals, risk tolerance, and current situation
- Provide educational insights about investment options
- Discuss both opportunities and potential risks
- Recommend consulting with licensed professionals for specific investment decisions
- Stay current with market trends and regulatory changes
- Be transparent about fees, risks, and limitations

When clients ask for investment advice, always:
1. Understand their current financial situation
2. Assess their risk tolerance
3. Identify their short and long-term goals
4. Provide educational context about options
5. Suggest next steps or areas to explore further

You're here to be their trusted financial advisor and help them make informed decisions about their wealth."""
        )

    @function_tool
    async def calculate_compound_interest(self, context: RunContext, principal: float, rate: float, time_years: float) -> str:
        """Calculate compound interest and future value for investment planning.
        
        Args:
            principal: Initial investment amount
            rate: Annual interest rate (as percentage, e.g., 7.0 for 7%)
            time_years: Investment time period in years
        """
        result = FinancialCalculator.compound_interest(principal, rate, time_years)
        return f"""Compound Interest Analysis:
- Initial Investment: ${result['principal']:,.2f}
- Annual Rate: {result['rate']}%
- Time Period: {result['time_years']} years
- Future Value: ${result['future_value']:,.2f}
- Interest Earned: ${result['interest_earned']:,.2f}
- Effective Annual Rate: {result['effective_annual_rate']}%

This shows the power of compound growth over time!"""

    @function_tool
    async def analyze_portfolio(self, context: RunContext, portfolio_json: str) -> str:
        """Analyze a client's investment portfolio for allocation and risk assessment.
        
        Args:
            portfolio_json: JSON string of portfolio holdings (e.g., '{"US Stocks": 50000, "Bonds": 30000}')
        """
        return analyze_client_portfolio(portfolio_json)

    @function_tool
    async def retirement_planning_analysis(self, context: RunContext, current_age: int, current_savings: float, 
                                         monthly_contribution: float, desired_income: float) -> str:
        """Comprehensive retirement planning analysis.
        
        Args:
            current_age: Client's current age
            current_savings: Current retirement savings
            monthly_contribution: Monthly contribution to retirement
            desired_income: Desired annual income in retirement
        """
        analysis = FinancialCalculator.retirement_planning(
            current_age=current_age,
            retirement_age=65,
            current_savings=current_savings,
            monthly_contribution=monthly_contribution,
            expected_return=7.0,
            desired_income=desired_income
        )
        
        return f"""Retirement Planning Analysis:
- Current Age: {analysis['current_age']}
- Years to Retirement: {analysis['years_to_retirement']}
- Current Savings: ${analysis['current_savings']:,.2f}
- Monthly Contribution: ${analysis['monthly_contribution']:,.2f}
- Desired Income: ${analysis['desired_income']:,.2f}

Projections:
- Future Value of Current Savings: ${analysis['future_savings']:,.2f}
- Future Value of Contributions: ${analysis['future_contributions']:,.2f}
- Total Retirement Savings: ${analysis['total_retirement_savings']:,.2f}
- Inflation-Adjusted Income Need: ${analysis['inflation_adjusted_income']:,.2f}
- Required Savings: ${analysis['required_savings']:,.2f}

Status: {'✅ ON TRACK!' if analysis['on_track'] else f'❌ SHORTFALL: ${analysis["shortfall"]:,.2f}'}

Recommendations:
- {'Increase monthly savings by $' + str(analysis['monthly_shortfall']) if not analysis['on_track'] else 'Continue current savings rate'}
- Consider increasing contributions annually
- Review investment allocation for optimal returns"""

    @function_tool
    async def mortgage_analysis(self, context: RunContext, loan_amount: float, interest_rate: float, 
                              loan_term_years: int, down_payment: float = 0) -> str:
        """Analyze mortgage options and payments.
        
        Args:
            loan_amount: Total loan amount
            interest_rate: Annual interest rate (as percentage)
            loan_term_years: Loan term in years
            down_payment: Down payment amount (optional)
        """
        result = FinancialCalculator.mortgage_calculator(loan_amount, interest_rate, loan_term_years, down_payment)
        
        return f"""Mortgage Analysis:
- Loan Amount: ${result['loan_amount']:,.2f}
- Down Payment: ${result['down_payment']:,.2f} ({result['down_payment_percentage']}%)
- Principal: ${result['principal']:,.2f}
- Interest Rate: {result['interest_rate']}%
- Loan Term: {result['loan_term_years']} years

Payment Breakdown:
- Monthly Payment: ${result['monthly_payment']:,.2f}
- Total Paid: ${result['total_paid']:,.2f}
- Total Interest: ${result['total_interest']:,.2f}

Considerations:
- Higher down payments reduce total interest paid
- Shorter terms increase monthly payments but reduce total cost
- Compare with investment returns on down payment funds"""

    @function_tool
    async def tax_efficiency_analysis(self, context: RunContext, income: float, filing_status: str, 
                                    investment_amount: float) -> str:
        """Provide tax-efficient investment recommendations.
        
        Args:
            income: Annual income
            filing_status: "single" or "married"
            investment_amount: Amount available for investment
        """
        result = FinancialCalculator.tax_efficient_investing(income, filing_status, investment_amount)
        
        return f"""Tax Efficiency Analysis:
- Annual Income: ${result['income']:,.2f}
- Filing Status: {result['filing_status'].title()}
- Marginal Tax Rate: {result['marginal_tax_rate']}%
- Investment Amount: ${result['investment_amount']:,.2f}
- Potential 401(k) Tax Savings: ${result['tax_savings_401k']:,.2f}

Recommendations:
{chr(10).join(['- ' + rec for rec in result['recommendations']])}

Tax-efficient investing can significantly impact your long-term returns!"""

    @function_tool
    async def investment_education(self, context: RunContext, topic: str) -> str:
        """Provide educational content on investment topics.
        
        Args:
            topic: Investment topic (diversification, compound_interest, risk_tolerance, retirement_planning)
        """
        education = MarketInsights.get_investment_education(topic)
        
        return f"""{education['title']}:

Key Points:
{chr(10).join(['- ' + point for point in education['key_points']])}

Example: {education['example']}

Understanding these concepts is crucial for building long-term wealth!"""

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(model="tts-1-hd", voice="echo"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )
    await session.start(
        room=ctx.room,
        agent=FinancialAdvisor(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )
    await ctx.connect()
    await session.generate_reply(
        instructions="Greet the client warmly and introduce yourself as Marcus Chen, their wealth management advisor. Speak with confidence and warmth, like a trusted family advisor. Ask about their financial goals and how you can help them today. Be professional, knowledgeable, and ready to provide valuable financial insights. Mention that you can perform real financial calculations and portfolio analysis to help them make informed decisions."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint)) 