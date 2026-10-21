from datetime import datetime
from zoneinfo import ZoneInfo
import src.finviz_fetch as ff

CSV1 = b"Ticker,Price\nAAPL,100\n"
CSV2 = b"Ticker,Price\nAAPL,200\n"


class _DT(datetime):
    fake = None

    @classmethod
    def now(cls, tz=None):
        return cls.fake.astimezone(tz) if tz else cls.fake


def _setup(tmp_path, monkeypatch):
    monkeypatch.setattr(ff, "SNAPSHOT_DIR", tmp_path)
    monkeypatch.setattr(ff, "ARCHIVE_DIR", tmp_path / "archive")
    monkeypatch.setattr(ff, "datetime", _DT)


def _at(h, m=0):
    _DT.fake = datetime(2026, 10, 21, h, m, tzinfo=ZoneInfo("America/New_York"))


def test_pre_close_archive_only_then_close_writes_dated(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch)
    _at(8, 30)
    ff.save_dated_snapshot(CSV1)
    assert not (tmp_path / "2026-10-21.csv").exists()
    assert not (tmp_path / "2026-10-21.raw.csv").exists()
    assert (tmp_path / "current.csv").exists()
    _at(16, 30)
    ff.save_dated_snapshot(CSV2)
    assert (tmp_path / "2026-10-21.raw.csv").read_bytes() == CSV2
    assert "200" in (tmp_path / "2026-10-21.csv").read_text()
    assert "200" in (tmp_path / "current.csv").read_text()
    assert "100" in (tmp_path / "previous.csv").read_text()


def test_later_run_never_overwrites_but_refreshes_current(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch)
    _at(16, 30)
    ff.save_dated_snapshot(CSV1)
    _at(17, 30)
    ff.save_dated_snapshot(CSV2)
    assert (tmp_path / "2026-10-21.raw.csv").read_bytes() == CSV1
    assert "100" in (tmp_path / "2026-10-21.csv").read_text()
    assert "200" in (tmp_path / "current.csv").read_text()
    assert "100" in (tmp_path / "previous.csv").read_text()
    assert len(list((tmp_path / "archive").glob("2026-10-21_*.raw.csv"))) == 2
