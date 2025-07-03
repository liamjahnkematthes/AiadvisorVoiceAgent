"""
Financial Analysis Tools for LiveKit Agent
Provides real financial calculations and insights
"""

import math
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json

class FinancialCalculator:
    """Comprehensive financial calculator with real-world formulas"""
    
    @staticmethod
    def compound_interest(principal: float, rate: float, time: float, compounds_per_year: int = 12) -> Dict:
        """Calculate compound interest and future value"""
        rate_decimal = rate / 100
        amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
        interest_earned = amount - principal
        
        return {
            "principal": principal,
            "rate": rate,
            "time_years": time,
            "compounds_per_year": compounds_per_year,
            "future_value": round(amount, 2),
            "interest_earned": round(interest_earned, 2),
            "effective_annual_rate": round(((1 + rate_decimal / compounds_per_year) ** compounds_per_year - 1) * 100, 2)
        }
    
    @staticmethod
    def retirement_planning(current_age: int, retirement_age: int, current_savings: float, 
                          monthly_contribution: float, expected_return: float, 
                          desired_income: float, inflation_rate: float = 2.5) -> Dict:
        """Comprehensive retirement planning analysis"""
        
        years_to_retirement = retirement_age - current_age
        years_in_retirement = 30  # Assume 30 years in retirement
        
        # Calculate future value of current savings
        future_savings = FinancialCalculator.compound_interest(
            current_savings, expected_return, years_to_retirement
        )["future_value"]
        
        # Calculate future value of monthly contributions
        monthly_rate = expected_return / 100 / 12
        total_contributions = monthly_contribution * 12 * years_to_retirement
        future_contributions = monthly_contribution * ((1 + monthly_rate) ** (years_to_retirement * 12) - 1) / monthly_rate
        
        total_retirement_savings = future_savings + future_contributions
        
        # Calculate inflation-adjusted desired income
        inflation_adjusted_income = desired_income * (1 + inflation_rate / 100) ** years_to_retirement
        
        # Calculate required retirement savings (4% rule)
        required_savings = inflation_adjusted_income * 25  # 4% withdrawal rate
        
        # Calculate shortfall or surplus
        shortfall = required_savings - total_retirement_savings
        
        return {
            "current_age": current_age,
            "retirement_age": retirement_age,
            "years_to_retirement": years_to_retirement,
            "current_savings": current_savings,
            "monthly_contribution": monthly_contribution,
            "expected_return": expected_return,
            "desired_income": desired_income,
            "future_savings": round(future_savings, 2),
            "future_contributions": round(future_contributions, 2),
            "total_retirement_savings": round(total_retirement_savings, 2),
            "inflation_adjusted_income": round(inflation_adjusted_income, 2),
            "required_savings": round(required_savings, 2),
            "shortfall": round(shortfall, 2),
            "on_track": shortfall <= 0,
            "monthly_shortfall": round(max(0, shortfall / (years_to_retirement * 12)), 2) if shortfall > 0 else 0
        }
    
    @staticmethod
    def mortgage_calculator(loan_amount: float, interest_rate: float, loan_term_years: int, 
                          down_payment: float = 0) -> Dict:
        """Calculate mortgage payments and amortization"""
        
        principal = loan_amount - down_payment
        monthly_rate = interest_rate / 100 / 12
        total_payments = loan_term_years * 12
        
        # Monthly payment formula
        if monthly_rate == 0:
            monthly_payment = principal / total_payments
        else:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
        
        total_paid = monthly_payment * total_payments
        total_interest = total_paid - principal
        
        return {
            "loan_amount": loan_amount,
            "down_payment": down_payment,
            "principal": principal,
            "interest_rate": interest_rate,
            "loan_term_years": loan_term_years,
            "monthly_payment": round(monthly_payment, 2),
            "total_paid": round(total_paid, 2),
            "total_interest": round(total_interest, 2),
            "down_payment_percentage": round((down_payment / loan_amount) * 100, 2)
        }
    
    @staticmethod
    def investment_portfolio_analysis(portfolio: Dict[str, float], 
                                    risk_free_rate: float = 2.0) -> Dict:
        """Analyze investment portfolio allocation and risk"""
        
        total_value = sum(portfolio.values())
        if total_value == 0:
            return {"error": "Portfolio is empty"}
        
        # Calculate allocation percentages
        allocation = {asset: (value / total_value) * 100 for asset, value in portfolio.items()}
        
        # Asset class categorization
        asset_classes = {
            "stocks": ["US Stocks", "International Stocks", "Emerging Markets", "Small Cap", "Large Cap"],
            "bonds": ["US Bonds", "Corporate Bonds", "Municipal Bonds", "Treasury Bonds"],
            "real_estate": ["REITs", "Real Estate", "Property"],
            "commodities": ["Gold", "Silver", "Oil", "Commodities"],
            "cash": ["Cash", "Money Market", "CDs"]
        }
        
        class_allocation = {"stocks": 0, "bonds": 0, "real_estate": 0, "commodities": 0, "cash": 0}
        
        for asset, percentage in allocation.items():
            for class_name, keywords in asset_classes.items():
                if any(keyword.lower() in asset.lower() for keyword in keywords):
                    class_allocation[class_name] += percentage
                    break
        
        # Risk assessment (simplified)
        risk_score = (
            class_allocation["stocks"] * 0.8 +
            class_allocation["real_estate"] * 0.6 +
            class_allocation["commodities"] * 0.7 +
            class_allocation["bonds"] * 0.3 +
            class_allocation["cash"] * 0.1
        ) / 100
        
        risk_level = "Conservative" if risk_score < 0.3 else "Moderate" if risk_score < 0.6 else "Aggressive"
        
        return {
            "total_value": total_value,
            "allocation": {k: round(v, 2) for k, v in allocation.items()},
            "asset_class_allocation": {k: round(v, 2) for k, v in class_allocation.items()},
            "risk_score": round(risk_score, 3),
            "risk_level": risk_level,
            "diversification_score": round(1 - max(allocation.values()) / 100, 3) if allocation else 0
        }
    
    @staticmethod
    def tax_efficient_investing(income: float, filing_status: str, 
                              investment_amount: float) -> Dict:
        """Provide tax-efficient investment recommendations"""
        
        # 2024 tax brackets (simplified)
        tax_brackets = {
            "single": [(11600, 0.10), (47150, 0.12), (100525, 0.22), (191950, 0.24), (243725, 0.32), (609350, 0.35), (float('inf'), 0.37)],
            "married": [(23200, 0.10), (94300, 0.12), (201050, 0.22), (383900, 0.24), (487450, 0.32), (731200, 0.35), (float('inf'), 0.37)]
        }
        
        brackets = tax_brackets.get(filing_status.lower(), tax_brackets["single"])
        
        # Calculate marginal tax rate
        marginal_rate = 0.10
        for threshold, rate in brackets:
            if income > threshold:
                marginal_rate = rate
        
        # Investment recommendations based on tax bracket
        recommendations = []
        
        if marginal_rate >= 0.24:
            recommendations.extend([
                "Maximize 401(k) contributions ($23,000 in 2024)",
                "Consider Traditional IRA for tax deduction",
                "Municipal bonds for tax-free income",
                "Tax-loss harvesting strategies"
            ])
        elif marginal_rate >= 0.22:
            recommendations.extend([
                "Balance between Traditional and Roth accounts",
                "Consider 401(k) matching first",
                "Tax-efficient index funds",
                "HSA contributions if eligible"
            ])
        else:
            recommendations.extend([
                "Roth IRA and Roth 401(k) for tax-free growth",
                "Tax-efficient ETFs and index funds",
                "Consider 401(k) for employer matching",
                "Focus on long-term capital gains"
            ])
        
        return {
            "income": income,
            "filing_status": filing_status,
            "marginal_tax_rate": round(marginal_rate * 100, 1),
            "investment_amount": investment_amount,
            "recommendations": recommendations,
            "tax_savings_401k": round(investment_amount * marginal_rate, 2) if investment_amount <= 23000 else round(23000 * marginal_rate, 2)
        }

class MarketInsights:
    """Provide market insights and educational content"""
    
    @staticmethod
    def get_investment_education(topic: str) -> Dict:
        """Provide educational content on investment topics"""
        
        education_content = {
            "diversification": {
                "title": "Portfolio Diversification",
                "key_points": [
                    "Don't put all your eggs in one basket",
                    "Mix different asset classes (stocks, bonds, real estate)",
                    "Consider international exposure",
                    "Rebalance periodically",
                    "Diversification reduces risk but doesn't eliminate it"
                ],
                "example": "A diversified portfolio might include 60% stocks, 30% bonds, and 10% real estate"
            },
            "compound_interest": {
                "title": "The Power of Compound Interest",
                "key_points": [
                    "Earnings generate more earnings over time",
                    "Time is your greatest ally",
                    "Start investing early, even with small amounts",
                    "Reinvest dividends and interest",
                    "Compound growth accelerates over decades"
                ],
                "example": "$10,000 invested at 7% for 30 years becomes $76,123"
            },
            "risk_tolerance": {
                "title": "Understanding Risk Tolerance",
                "key_points": [
                    "Conservative: 20-40% stocks, focus on capital preservation",
                    "Moderate: 40-70% stocks, balanced growth and safety",
                    "Aggressive: 70-100% stocks, maximum growth potential",
                    "Consider your time horizon and emotional comfort",
                    "Risk tolerance can change over time"
                ],
                "example": "Young investors can afford more risk due to longer time horizons"
            },
            "retirement_planning": {
                "title": "Retirement Planning Fundamentals",
                "key_points": [
                    "Calculate your retirement number (25x annual expenses)",
                    "Maximize employer retirement accounts",
                    "Consider healthcare costs in retirement",
                    "Plan for multiple income sources",
                    "Start early and increase contributions over time"
                ],
                "example": "If you need $80,000/year in retirement, aim for $2 million saved"
            }
        }
        
        return education_content.get(topic.lower(), {
            "title": "Investment Education",
            "key_points": ["Contact your advisor for personalized guidance"],
            "example": "Every investor's situation is unique"
        })

# Example usage functions for the agent
def analyze_client_portfolio(portfolio_data: str) -> str:
    """Analyze a client's portfolio and provide insights"""
    try:
        portfolio = json.loads(portfolio_data)
        analysis = FinancialCalculator.investment_portfolio_analysis(portfolio)
        
        return f"""Portfolio Analysis:
- Total Value: ${analysis['total_value']:,.2f}
- Risk Level: {analysis['risk_level']} (Score: {analysis['risk_score']})
- Diversification Score: {analysis['diversification_score']}

Asset Allocation:
{chr(10).join([f"- {asset}: {percentage:.1f}%" for asset, percentage in analysis['allocation'].items()])}

Recommendations:
- {'Consider increasing diversification' if analysis['diversification_score'] < 0.7 else 'Good diversification'}
- {'Review risk tolerance' if analysis['risk_score'] > 0.7 else 'Risk level appears appropriate'}
- Rebalance portfolio annually"""
    except:
        return "Unable to analyze portfolio. Please provide portfolio data in JSON format."

def calculate_retirement_needs(age: int, current_savings: float, desired_income: float) -> str:
    """Calculate retirement planning needs"""
    analysis = FinancialCalculator.retirement_planning(
        current_age=age,
        retirement_age=65,
        current_savings=current_savings,
        monthly_contribution=1000,
        expected_return=7.0,
        desired_income=desired_income
    )
    
    return f"""Retirement Analysis:
- Years to Retirement: {analysis['years_to_retirement']}
- Projected Savings: ${analysis['total_retirement_savings']:,.2f}
- Required Savings: ${analysis['required_savings']:,.2f}
- {'On Track!' if analysis['on_track'] else f'Shortfall: ${analysis["shortfall"]:,.2f}'}

Recommendations:
- {'Increase monthly savings by $' + str(analysis['monthly_shortfall']) if not analysis['on_track'] else 'Continue current savings rate'}
- Consider increasing contributions annually
- Review investment allocation for optimal returns""" 