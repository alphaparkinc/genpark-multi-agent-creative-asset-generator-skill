from client import MultiAgentCreativeAssetGeneratorClient

def main():
    client = MultiAgentCreativeAssetGeneratorClient()
    res = client.generate_creative_assets("Launch of GenPark 2.0 AI Agent OS", ["Twitter", "LinkedIn"])
    print(f"Status: {res['campaign_status']}")
    print("Copy Variants:", res["generated_copy_variants"])

if __name__ == "__main__":
    main()
