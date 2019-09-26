from aqt import mw
from aqt.utils import showWarning, tooltip
from anki.utils import guid64
from anki.lang import _
from aqt.qt import QAction, QKeySequence

def ensure():
    mw.checkpoint("Unique GUID")
    lastGuid = None
    nids = []
    lastNid = None
    for guid, nid in mw.col.db.all("select guid, id from notes order by guid"):
        if lastGuid == guid:
            mw.col.modSchema(True)
            mw.col.db.execute("update notes set guid = ? where id = ? ", guid64(), nid)
            nids.append((nid,lastNid))
        lastGuid = guid
        lastNid = nid
    if nids:
        s = _("The guid of the following notes have been changed:")
        s+= "\n".join(_("Note %d which was a copy of note %d")%(nid, lastNid) for nid, lastNid in nids)
        showWarning(s)
    else:
        tooltip(_("Each guid was unique. No correction required"))


action = QAction(mw)
action.setText("Ensure unique GUID")
mw.form.menuTools.addAction(action)
action.triggered.connect(ensure)

