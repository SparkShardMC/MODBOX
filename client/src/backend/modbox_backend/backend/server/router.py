from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"service": "MODBOX Backend"}

@router.post("/signup")
async def signup():
    return {"status": "signup endpoint"}

@router.post("/oauth/google")
async def oauth_google():
    return {"provider": "google"}

@router.post("/oauth/microsoft")
async def oauth_microsoft():
    return {"provider": "microsoft"}

@router.post("/oauth/apple")
async def oauth_apple():
    return {"provider": "apple"}

@router.post("/send-verification-code")
async def send_verification():
    return {"status": "code sent"}

@router.post("/verify-code")
async def verify_code():
    return {"status": "verification endpoint"}

@router.post("/parent-request")
async def parent_request():
    return {"status": "parent request sent"}

@router.post("/parent-response")
async def parent_response():
    return {"status": "parent response received"}
