knowledge = {

"clinical trial":
"Clinical trials evaluate safety and effectiveness of new treatments.",

"inclusion":
"Inclusion criteria define conditions required to participate in trials.",

"exclusion":
"Exclusion criteria prevent patients with certain risks from participating.",

"twin":
"Twin AI compares synthetic patients with real patient records to suggest eligibility improvements.",

"omnimatch":
"OmniMatch ranks trials using clinical fit, operational suitability, and health readiness."
}

def ask_ai(query):

    q=query.lower()

    for k in knowledge:

        if k in q:
            return knowledge[k]

    return "OmniMatch AI analyzes patient eligibility and ranks clinical trials."