ALLOWED = {"draft":{"review"}, "review":{"published","draft"}, "published":{"archived"}, "archived":set()}

def transition(current: str, requested: str) -> tuple[str, str]:
    if requested in ALLOWED.get(current, set()):
        return requested, f"accepted transition from {current} to {requested}"
    return current, f"rejected transition from {current} to {requested}"

def demo_state_machine() -> dict[str, object]:
    state="draft"; history=[]
    for requested in ["review","published","draft","archived"]:
        next_state,msg = transition(state, requested)
        history.append({"from":state,"requested":requested,"to":next_state,"message":msg})
        state = next_state
    return {"initial_state":"draft","final_state":state,"history":history}

def aliasing_demo() -> dict[str, object]:
    original={"items":["draft"]}; alias=original; copied={"items":list(original["items"])}
    alias["items"].append("review"); copied["items"].append("published")
    return {"original":original,"alias":alias,"copied":copied}
