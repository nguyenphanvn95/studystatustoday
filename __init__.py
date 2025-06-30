
from aqt.deckbrowser import *
from .path_manager import MESSAGE_TEMPLATE, check_custom_text


def _renderStats_3(self:"DeckBrowser") -> str:
    try:
        config = self.mw.addonManager.getConfig(__name__)

        use_distinct = config.get("use_distinct_count", False)
        if use_distinct:
            count_clause = "count(DISTINCT cid)"
        else:
            count_clause = "count(cid)"

        sql_query = f"""
        SELECT
            {count_clause},
            sum(time)/1000
        FROM revlog
        WHERE id > ?
        """

        if hasattr(self.mw.col.sched, "day_cutoff"):
            day_cutoff = self.mw.col.sched.day_cutoff
        else:
            day_cutoff = self.mw.col.sched.dayCutoff

        cutoff_time = (day_cutoff - 86400) * 1000
        cards, thetime = self.mw.col.db.first(sql_query, cutoff_time)

        card_text = cards or 0
        thetime = thetime or 0

        try:
            time_text = self.mw.col.format_timespan(thetime, context=0)
            # print(time_text)
        except Exception as e:
            print(e)
            from anki.utils import fmtTimeSpan
            time_text = fmtTimeSpan(thetime, unit=1)

        if cards > 0:
            avg_seconds = thetime / cards
            # avg_text = f" ({avg_seconds:.1f}s/card)"
            avg_text = f"{avg_seconds:.1f}"
        else:
            avg_text = "0"

        custom_text = config.get("custom_text", MESSAGE_TEMPLATE) #type: str

        custom_text = check_custom_text(custom_text)

        studied_today = custom_text.format(
            card_text=card_text,
            time_text=time_text,
            avg_text=avg_text
        )

        studied_today = f"""<a href=#
        onclick="pycmd('shige_rewrite_study_cards_text'); return false;"
        style="color: inherit; text-decoration: none;">{studied_today}</a>"""
        return studied_today
    except Exception as e:
        print(e)
        return '<div id="studiedToday"><span>{}</span></div>'.format(
            self._render_data.studied_today
        )

orig__renderStats = DeckBrowser._renderStats
DeckBrowser._renderStats = _renderStats_3

def handleMyAddonConfig(handled, message, context):
    if message == "shige_rewrite_study_cards_text":
        from .shige_config.addon_config import setMyAddonConfig
        QTimer.singleShot(0, setMyAddonConfig)
        return (True, None)
    else:
        return handled

gui_hooks.webview_did_receive_js_message.append(handleMyAddonConfig)