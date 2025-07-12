#!/usr/bin/env python
import sys
import warnings

from datetime import datetime



from contract.crew import ContractReviewTeam


def run():
    """
    Run the Contract Review Team crew.
    """
    # Example contract input – replace this with actual contract text or file loading
    inputs = {
        'input': """Service Agreement

This Service Agreement ("Agreement") is made effective as of July 1, 2025, by and between AlphaTech Solutions ("Client") and NovaWorks Pvt. Ltd. ("Service Provider").

1. Scope of Work:
The Service Provider agrees to design, develop, and deliver a cloud-based inventory management system for the Client within 90 days of the Agreement's effective date.

2. Payment Terms:
The total fee for services shall be INR 12,00,000, payable in three installments:
- 30% upon signing this Agreement
- 40% upon mid-project milestone completion
- 30% upon final delivery

3. Penalties and Late Delivery:
For every week of delay beyond the delivery date, a penalty of INR 20,000 shall be applied unless the delay is due to reasons beyond the Service Provider’s control.

4. Confidentiality:
Both parties agree to maintain confidentiality of all sensitive business information received during the course of this Agreement.

5. Termination:
Either party may terminate this Agreement with 30 days’ written notice. Upon termination, the Client will pay for all work completed up to the date of termination.

6. Liability:
The Service Provider’s liability for any claims shall not exceed the total amount paid under this Agreement.

7. Governing Law:
This Agreement shall be governed by the laws of the Republic of India.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first written above.
"""
    }

    try:
        result = ContractReviewTeam().crew().kickoff(inputs=inputs)
        print("\n📄 Final Contract Review Output:\n")
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


