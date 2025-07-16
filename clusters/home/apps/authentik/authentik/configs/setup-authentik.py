import os
import time
import requests

AUTHENTIK_API_URL = os.environ["AUTHENTIK_API_URL"]
AUTHENTIK_URL = os.environ["AUTHENTIK_URL"]
AUTHENTIK_TOKEN = os.environ["AUTHENTIK_BOOTSTRAP_TOKEN"]
HEADERS = {
    "Authorization": f"Bearer {AUTHENTIK_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def wait_for_ready():
    print("Waiting for Authentik to be ready...")
    while True:
        try:
            r = requests.get(f"{AUTHENTIK_URL}/-/health/ready/")
            if r.ok:
                break
        except Exception:
            pass
        time.sleep(30)
    print("✅ Authentik is ready.")


def get_id(url, key="pk"):
    r = requests.get(url, headers=HEADERS).json()
    return r["results"][0][key] if r.get("results") else None


def create_or_get(url, payload, key="pk"):
    r = requests.get(f"{url}?search={payload['name']}", headers=HEADERS).json()
    if r.get("results"):
        print(f"✅ Found {payload['name']}")
        return r["results"][0][key]
    print(f"Creating {payload['name']}...")
    r = requests.post(url, headers=HEADERS, json=payload).json()
    return r[key]


if __name__ == "__main__":
    wait_for_ready()
    flow_id = get_id(
        f"{AUTHENTIK_API_URL}/flows/instances/?slug=default-provider-authorization-implicit-consent"
    )
    if not flow_id:
        print("❌ Missing flow")
        exit(1)

    provider_id = create_or_get(
        f"{AUTHENTIK_API_URL}/providers/proxy/",
        {
            "name": "podinfo-forwardauth",
            "authorization_flow": flow_id,
            "external_host": "https://podinfo.homelab.rivetcode.com",
            "mode": "forward_single",
            "cookie_domain": "homelab.rivetcode.com",
            "preserve_path": True,
        },
    )

    outpost_id = create_or_get(
        f"{AUTHENTIK_API_URL}/outposts/instances/",
        {"name": "authentik-outpost", "type": "proxy"},
    )

    app_id = create_or_get(
        f"{AUTHENTIK_API_URL}/core/applications/",
        {
            "name": "podinfo",
            "slug": "podinfo",
            "provider": f"/api/v3/providers/proxy/{provider_id}/",
            "authorization_flow": flow_id,
            "meta_launch_url": "https://podinfo.homelab.rivetcode.com",
            "outpost": f"/api/v3/outposts/{outpost_id}/",
        },
    )

    print("🎉 Authentik setup complete.")
