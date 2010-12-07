from product_details import product_details
from tower import ugettext_lazy as _


# Applications, shamelessly snagged from AMO
class FIREFOX:
    id = 1
    short = 'firefox'
    pretty = _(u'Firefox')
    guid = '{ec8030f7-c20a-464f-9b0e-13a3a9e97384}'
    hide_below = '4.0b1'

class MOBILE:
    id = 60
    short = 'mobile'
    pretty = _(u'Mobile')
    guid = '{a23983c0-fd0e-11dc-95ff-0800200c9a66}'

APP_USAGE = _apps = (FIREFOX, MOBILE)
APPS = dict((app.short, app) for app in _apps)
APP_IDS = dict((app.id, app) for app in _apps)

UA_PATTERN_FIREFOX = (
    r'^Mozilla.*(Firefox|Minefield|Namoroka|Shiretoko|GranParadiso|BonEcho|'
    'Iceweasel|Fennec|MozillaDeveloperPreview)\/([^\s]*).*$')
UA_PATTERN_MOBILE = r'^Mozilla.*(Fennec)\/([^\s]*)$'

# Order is important: Since Fennec is Firefox too, it'll match the second
# pattern as well, so we must detect it first.
BROWSERS = (
    (MOBILE, UA_PATTERN_MOBILE),
    (FIREFOX, UA_PATTERN_FIREFOX),
)

LATEST_BETAS = {
    FIREFOX: product_details.firefox_versions['LATEST_FIREFOX_RELEASED_DEVEL_VERSION'],
    MOBILE: product_details.mobile_details['beta_version'],
}

# Operating Systems
class WINDOWS_XP:
    pretty = _(u'Windows XP')
    short = 'winxp'
    ua_pattern = 'Windows NT 5.1'
    apps = set((FIREFOX,))

class WINDOWS_7:
    pretty = _(u'Windows 7')
    short = 'win7'
    ua_pattern = 'Windows NT 6.1'
    apps = set((FIREFOX,))

class WINDOWS_VISTA:
    pretty = _(u'Windows Vista')
    short = 'vista'
    ua_pattern = 'Windows NT 6.0'
    apps = set((FIREFOX,))

class OSX:
    pretty = _(u'Mac OS X')
    short = 'mac'
    ua_pattern = 'Mac'
    apps = set((FIREFOX,))

class MAEMO:
    pretty = _('Maemo')
    short = 'maemo'
    ua_pattern = 'Maemo'
    apps = set((MOBILE,))

class ANDROID:
    pretty = _('Android')
    short = 'android'
    ua_pattern = 'Android'
    apps = set((MOBILE,))

class LINUX:
    pretty = _(u'Linux')
    short = 'linux'
    ua_pattern = 'Linux'
    apps = set((FIREFOX,))

class OS_OTHER:
    pretty = _(u'Other')
    short = 'other'
    ua_pattern = None
    apps = set((FIREFOX, MOBILE))

OS_USAGE = _oses = (WINDOWS_XP, WINDOWS_VISTA, WINDOWS_7, OSX, MAEMO, ANDROID,
                    LINUX)
OS_PATTERNS = [(o.ua_pattern, o.short) for o in OS_USAGE]
OSES = dict((os.short, os) for os in _oses)

# Opinion Types
OPINION_PRAISE = 1
OPINION_ISSUE = 2
OPINION_SUGGESTION = 3
OPINION_RATING = 4
OPINION_BROKEN = 5

OPINION_TYPES = {
    OPINION_PRAISE: _(u'Praise'),
    OPINION_ISSUE: _(u'Issue'),
    OPINION_SUGGESTION: _(u'Suggestion'),
    OPINION_RATING: _(u'Rating'),
    OPINION_BROKEN: _(u'Broken Website'),
}

# Rating Types
RATING_STARTUP = 1
RATING_PAGELOAD = 2
RATING_RESPONSIVE = 3
RATING_CRASHY = 4
RATING_FEATURES = 5

RATING_USAGE = (RATING_STARTUP, RATING_PAGELOAD, RATING_RESPONSIVE,
                RATING_CRASHY, RATING_FEATURES)
RATING_TYPES = {
    RATING_STARTUP: {
        'short': 'startup',
        'name': _(u'Start-Up Time'),
        'help': _(u'How long Firefox takes to start running'),
    },
    RATING_PAGELOAD: {
        'short': 'pageload',
        'name': _(u'Page Load Time'),
        'help': _(u'How long it takes for web pages to load'),
    },
    RATING_RESPONSIVE: {
        'short': 'responsive',
        'name': _(u'Responsiveness'),
         'help': _(u'How quickly web pages respond once they have loaded'),
    },
    RATING_CRASHY: {
        'short': 'crashy',
        'name': _(u'Crashiness'),
        'help': _(u'How frequently Firefox crashes or loses data'),
    },
    RATING_FEATURES: {
        'short': 'features',
        'name': _(u'Features'),
        'help': _(u"How well Firefox's built-in features serve your needs"),
    },
}
RATING_CHOICES = (
    (1, _(u'Poor')),
    (2, _(u'Fair')),
    (3, _(u"Don't Care")),
    (4, _(u'Good')),
    (5, _(u'Excellent')),
)
