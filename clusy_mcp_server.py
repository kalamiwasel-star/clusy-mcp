
from pathlib import Path
from mcp.server.fastmcp import FastMCP
import importlib.util

ROOT = Path("/mnt/workspace/clusy_agent")
BRIDGE_FILE = ROOT / "core" / "gpt_clusy_bridge_v1.py"

spec = importlib.util.spec_from_file_location(
    "gpt_clusy_bridge_v1",
    BRIDGE_FILE
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

bridge = mod.GPTClusyBridgeV1(str(ROOT))

mcp = FastMCP(
    "CLUSY",
    instructions=(
        "CLUSY scientific bridge controlled by GPT. "
        "Human approval is required before execution."
    ),
)

@mcp.tool()
def clusy_inspect() -> dict:
    """Read-only CLUSY state."""
    return bridge.inspect_state()

@mcp.tool()
def clusy_health() -> dict:
    """Read-only CLUSY health."""
    return bridge.health()

@mcp.tool()
def clusy_propose(
    request: str,
    layer: str = "scientific",
    tool: str = "auto",
) -> dict:
    """Submit a proposal. Does not execute."""
    return bridge.submit_proposal({
        "request": request,
        "layer": layer,
        "tool": tool,
    })

@mcp.tool()
def clusy_approve(
    proposal_id: str,
    approved: bool = True,
) -> dict:
    """Human approval/rejection for a proposal."""
    return bridge.approve(
        proposal_id,
        approved=approved,
    )

@mcp.tool()
def clusy_get_result(result_path: str) -> dict:
    """Read a CLUSY result."""
    return bridge.get_result(result_path)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
