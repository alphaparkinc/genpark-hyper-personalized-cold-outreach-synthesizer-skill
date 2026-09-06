import json
from client import HyperPersonalizedOutreachSynthesizer

def main():
    synthesizer = HyperPersonalizedOutreachSynthesizer()
    prospect = {"first_name": "Marcus", "title": "Head of Revenue Operations"}
    company = {"name": "Starlight Logistics", "industry": "Supply Chain SaaS"}
    catalyst = {"headline": "Series B Funding Announcement", "pain_area": "lead routing latency"}
    value_prop = "automate lead enrichment and qualification with zero engineering maintenance"
    
    sequence = synthesizer.generate_outreach_sequence(prospect, company, catalyst, value_prop)
    print("Generated Outreach Sequence:")
    print(json.dumps(sequence, indent=2))
    assert sequence["sequence_touch_count"] == 3
    assert sequence["cadence"][0]["spam_audit"]["is_clean"] is True
    print("Outreach synthesizer verification complete: PASS")

if __name__ == "__main__":
    main()
