import re
from typing import Dict, Any, List

class HyperPersonalizedOutreachSynthesizer:
    """
    Generates multi-touch outbound cadences dynamically structured around prospect role, company catalysts, and pain points.
    Includes automated spam trigger word filtering and tone adaptation.
    """
    SPAM_TRIGGERS = [
        "100% free", "risk-free", "double your income", "act now", "make money fast",
        "guaranteed", "no credit check", "miracle", "urgently need"
    ]

    def check_spam_score(self, text: str) -> Dict[str, Any]:
        low = text.lower()
        found = [trigger for trigger in self.SPAM_TRIGGERS if trigger in low]
        return {
            "is_clean": len(found) == 0,
            "detected_triggers": found,
            "spam_penalty_points": len(found) * 15
        }

    def generate_outreach_sequence(
        self,
        prospect: Dict[str, Any],
        company: Dict[str, Any],
        catalyst: Dict[str, Any],
        value_proposition: str
    ) -> Dict[str, Any]:
        first_name = prospect.get("first_name", "there")
        title = prospect.get("title", "leader")
        company_name = company.get("name", "your team")
        industry = company.get("industry", "tech")
        trigger_event = catalyst.get("headline", "recent expansion")

        # Touch 1: Contextual Hook & Pain Hypothesis
        subject_1 = f"Idea for {company_name}'s {trigger_event.lower()}"
        touch_1 = (
            f"Hi {first_name},\n\n"
            f"Noticed {company_name}'s {trigger_event} -- congratulations to you and the team.\n\n"
            f"As {title}, scaling operations during this phase often introduces friction around "
            f"{catalyst.get('pain_area', 'workflow bottlenecks')}. We built a framework to {value_proposition} "
            f"without requiring headcount overhead.\n\n"
            f"Worth exploring how peers in {industry} approached this, or is this already solved on your end?\n\n"
            f"Best regards,"
        )

        # Touch 2: Metric Benchmark & Social Proof (Day 3)
        subject_2 = f"Re: Idea for {company_name}'s {trigger_event.lower()}"
        touch_2 = (
            f"Hi {first_name},\n\n"
            f"Following up briefly on my previous note. Similar teams in {industry} reduced manual cycle times "
            f"by 42% in the first quarter of adoption.\n\n"
            f"Here is a 60-second summary breakdown if relevant to your current quarterly objectives: "
            f"https://genpark.ai/case-study\n\n"
            f"Happy to share the exact playbook if you're open to a 7-minute exchange."
        )

        # Touch 3: Permission to Close Loop / Breakup (Day 7)
        subject_3 = f"Closing loop on {company_name}"
        touch_3 = (
            f"Hi {first_name},\n\n"
            f"I assume {catalyst.get('pain_area', 'this area')} isn't a high priority for {company_name} right now, "
            f"which makes complete sense with your current focus on {trigger_event}.\n\n"
            f"I won't clutter your inbox further. If priorities shift later this quarter, feel free to reach back out.\n\n"
            f"Wishing you and {company_name} continued momentum."
        )

        touches = [
            {"step": 1, "day": 1, "channel": "Email", "subject": subject_1, "body": touch_1},
            {"step": 2, "day": 4, "channel": "Email", "subject": subject_2, "body": touch_2},
            {"step": 3, "day": 8, "channel": "Email", "subject": subject_3, "body": touch_3}
        ]

        # Audit spam compliance
        for t in touches:
            t["spam_audit"] = self.check_spam_score(t["subject"] + " " + t["body"])

        return {
            "prospect_name": f"{first_name} ({title})",
            "company": company_name,
            "sequence_touch_count": len(touches),
            "cadence_days": 8,
            "cadence": touches
        }
