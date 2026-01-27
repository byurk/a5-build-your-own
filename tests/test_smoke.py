from ai_in_loop.doctor import collect_info
from ai_in_loop.config import Config
from ai_in_loop.graph import run_once


def test_doctor_collects_info():
    info = collect_info()
    assert "python_version" in info
    assert "packages" in info


def test_graph_runs_with_mock():
    cfg = Config(
        use_gemini=False,
        gemini_api_key=None,
        gemini_model="gemini-2.5-flash",
        temperature=0.7,
        thinking_level=None,
        thinking_budget=0,
        system_prompt_file="prompts/empty.md",
        resources_dir="resources",
        chunk_size=1000,
        chunk_overlap=100,
    )
    out = run_once("hello", cfg)
    assert isinstance(out, str)
    assert out.startswith("[MOCK]")
