import string

from .reader import DaapNumericReader
from .request import DaapStringIO
class DmapFieldType(object):
    """This class is just a simple enum
    Returns the content type of each instruction
    """
    values = ('DMAP_UNKNOWN', 'DMAP_UINT', 'DMAP_INT', 'DMAP_STR',
              'DMAP_DATA', 'DMAP_DATE', 'DMAP_VERS', 'DMAP_DICT')

    @classmethod
    def name(cls, idx):
        """Return enum value as string
        """
        return cls.values[idx] if idx < len(cls.values) else None

    class __metaclass__(type):
        """Define __getattr__ of metaclass to directly use
        without an instance"""
        def __getattr__(self, name):
            return self.values.index(name)

class DmapFieldNotFound(Exception):
    """Raised when DMAP field type extracted from buffer is not implemented
    """

class DmapInstruction(object):
    """Get content type and verbose name of a dmap instruction
    Read ```parse``` method below to understand what is the use.
    """
    data = {
        'abal': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.browsealbumlisting'},
        'abar': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.browseartistlisting'},
        'abcp': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.browsecomposerlisting'},
        'abgn': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.browsegenrelisting'},
        'abpl': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.baseplaylist'},
        'abro': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.databasebrowse'},
        'adbs': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.databasesongs'},
        'aeAD': {'type': DmapFieldType.DMAP_DICT, 'name': 'com.apple.itunes.adam-ids-array'},
        'aeAI': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.itms-artistid'},
        'aeCD': {'type': DmapFieldType.DMAP_DATA, 'name': 'com.apple.itunes.flat-chapter-data'},
        'aeCF': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.cloud-flavor-id'},
        'aeCI': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.itms-composerid'},
        'aeCK': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.cloud-library-kind'},
        'aeCM': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.cloud-status'},
        'aeCR': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.content-rating'},
        'aeCS': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.artworkchecksum'},
        'aeCU': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.cloud-user-id'},
        'aeCd': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.cloud-id'},
        'aeDP': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.drm-platform-id'},
        'aeDR': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.drm-user-id'},
        'aeDV': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.drm-versions'},
        'aeEN': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.episode-num-str'},
        'aeES': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.episode-sort'},
        'aeGD': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.gapless-enc-dr'},
        'aeGE': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.gapless-enc-del'},
        'aeGH': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.gapless-heur'},
        'aeGI': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.itms-genreid'},
        'aeGR': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.gapless-resy'},
        'aeGU': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.gapless-dur'},
        'aeGs': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.can-be-genius-seed'},
        'aeHC': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.has-chapter-data'},
        'aeHD': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.is-hd-video'},
        'aeHV': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.has-video'},
        'aeK1': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.drm-key1-id'},
        'aeK2': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.drm-key2-id'},
        'aeMC': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.playlist-contains-media-type-count'},
        'aeMK': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.mediakind'},
        'aeMX': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.movie-info-xml'},
        'aeMk': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.extended-media-kind'},
        'aeND': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.non-drm-user-id'},
        'aeNN': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.network-name'},
        'aeNV': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.norm-volume'},
        'aePC': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.is-podcast'},
        'aePI': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.itms-playlistid'},
        'aePP': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.is-podcast-playlist'},
        'aePS': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.special-playlist'},
        'aeRD': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.rental-duration'},
        'aeRP': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.rental-pb-start'},
        'aeRS': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.rental-start'},
        'aeRU': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.rental-pb-duration'},
        'aeSE': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.store-pers-id'},
        'aeSF': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.itms-storefrontid'},
        'aeSG': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.saved-genius'},
        'aeSI': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.itms-songid'},
        'aeSN': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.series-name'},
        'aeSP': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.smart-playlist'},
        'aeSU': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.season-num'},
        'aeSV': {'type': DmapFieldType.DMAP_VERS, 'name': 'com.apple.itunes.music-sharing-version'},
        'aeXD': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.xid'},
        'aemi': {'type': DmapFieldType.DMAP_DICT, 'name': 'com.apple.itunes.media-kind-listing-item'},
        'aeml': {'type': DmapFieldType.DMAP_DICT, 'name': 'com.apple.itunes.media-kind-listing'},
        'agac': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.groupalbumcount'},
        'agma': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.groupmatchedqueryalbumcount'},
        'agmi': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.groupmatchedqueryitemcount'},
        'agrp': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songgrouping'},
        'aply': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.databaseplaylists'},
        'aprm': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.playlistrepeatmode'},
        'apro': {'type': DmapFieldType.DMAP_VERS, 'name': 'daap.protocolversion'},
        'apsm': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.playlistshufflemode'},
        'apso': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.playlistsongs'},
        'arif': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.resolveinfo'},
        'arsv': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.resolve'},
        'asaa': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songalbumartist'},
        'asac': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songartworkcount'},
        'asai': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songalbumid'},
        'asal': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songalbum'},
        'asar': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songartist'},
        'asas': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songalbumuserratingstatus'},
        'asbk': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.bookmarkable'},
        'asbo': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songbookmark'},
        'asbr': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songbitrate'},
        'asbt': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songbeatsperminute'},
        'ascd': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songcodectype'},
        'ascm': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songcomment'},
        'ascn': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songcontentdescription'},
        'asco': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songcompilation'},
        'ascp': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songcomposer'},
        'ascr': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songcontentrating'},
        'ascs': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songcodecsubtype'},
        'asct': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songcategory'},
        'asda': {'type': DmapFieldType.DMAP_DATE, 'name': 'daap.songdateadded'},
        'asdb': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songdisabled'},
        'asdc': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songdisccount'},
        'asdk': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songdatakind'},
        'asdm': {'type': DmapFieldType.DMAP_DATE, 'name': 'daap.songdatemodified'},
        'asdn': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songdiscnumber'},
        'asdp': {'type': DmapFieldType.DMAP_DATE, 'name': 'daap.songdatepurchased'},
        'asdr': {'type': DmapFieldType.DMAP_DATE, 'name': 'daap.songdatereleased'},
        'asdt': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songdescription'},
        'ased': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songextradata'},
        'aseq': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songeqpreset'},
        'ases': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songexcludefromshuffle'},
        'asfm': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songformat'},
        'asgn': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songgenre'},
        'asgp': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songgapless'},
        'asgr': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.supportsgroups'},
        'ashp': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songhasbeenplayed'},
        'askd': {'type': DmapFieldType.DMAP_DATE, 'name': 'daap.songlastskipdate'},
        'askp': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songuserskipcount'},
        'asky': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songkeywords'},
        'aslc': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songlongcontentdescription'},
        'aslr': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songalbumuserrating'},
        'asls': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songlongsize'},
        'aspc': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songuserplaycount'},
        'aspl': {'type': DmapFieldType.DMAP_DATE, 'name': 'daap.songdateplayed'},
        'aspu': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songpodcasturl'},
        'asri': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songartistid'},
        'asrs': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songuserratingstatus'},
        'asrv': {'type': DmapFieldType.DMAP_INT, 'name': 'daap.songrelativevolume'},
        'assa': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.sortartist'},
        'assc': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.sortcomposer'},
        'assl': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.sortalbumartist'},
        'assn': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.sortname'},
        'assp': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songstoptime'},
        'assr': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songsamplerate'},
        'asss': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.sortseriesname'},
        'asst': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songstarttime'},
        'assu': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.sortalbum'},
        'assz': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songsize'},
        'astc': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songtrackcount'},
        'astm': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songtime'},
        'astn': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songtracknumber'},
        'asul': {'type': DmapFieldType.DMAP_STR, 'name': 'daap.songdataurl'},
        'asur': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songuserrating'},
        'asvc': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songprimaryvideocodec'},
        'asyr': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.songyear'},
        'ated': {'type': DmapFieldType.DMAP_UINT, 'name': 'daap.supportsextradata'},
        'avdb': {'type': DmapFieldType.DMAP_DICT, 'name': 'daap.serverdatabases'},
        'caar': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.availablerepeatstates'},
        'caas': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.availableshufflestates'},
        'caci': {'type': DmapFieldType.DMAP_DICT, 'name': 'caci'},
        'cafe': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.fullscreenenabled'},
        'cafs': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.fullscreen'},
        'caia': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.isactive'},
        'cana': {'type': DmapFieldType.DMAP_STR, 'name': 'dacp.nowplayingartist'},
        'cang': {'type': DmapFieldType.DMAP_STR, 'name': 'dacp.nowplayinggenre'},
        'canl': {'type': DmapFieldType.DMAP_STR, 'name': 'dacp.nowplayingalbum'},
        'cann': {'type': DmapFieldType.DMAP_STR, 'name': 'dacp.nowplayingname'},
        'canp': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.nowplayingids'},
        'cant': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.nowplayingtime'},
        'capr': {'type': DmapFieldType.DMAP_VERS, 'name': 'dacp.protocolversion'},
        'caps': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.playerstate'},
        'carp': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.repeatstate'},
        'cash': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.shufflestate'},
        'casp': {'type': DmapFieldType.DMAP_DICT, 'name': 'dacp.speakers'},
        'cast': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.songtime'},
        'cavc': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.volumecontrollable'},
        'cave': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.visualizerenabled'},
        'cavs': {'type': DmapFieldType.DMAP_UINT, 'name': 'dacp.visualizer'},
        'ceJC': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.jukebox-client-vote'},
        'ceJI': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.jukebox-current'},
        'ceJS': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.jukebox-score'},
        'ceJV': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.jukebox-vote'},
        'ceQR': {'type': DmapFieldType.DMAP_DICT, 'name': 'com.apple.itunes.playqueue-contents-response'},
        'ceQa': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.playqueue-album'},
        'ceQg': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.playqueue-genre'},
        'ceQn': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.playqueue-name'},
        'ceQr': {'type': DmapFieldType.DMAP_STR, 'name': 'com.apple.itunes.playqueue-artist'},
        'cmgt': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmcp.getpropertyresponse'},
        'cmmk': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmcp.mediakind'},
        'cmpr': {'type': DmapFieldType.DMAP_VERS, 'name': 'dmcp.protocolversion'},
        'cmsr': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmcp.serverrevision'},
        'cmst': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmcp.playstatus'},
        'cmvo': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmcp.volume'},
        'ipsa': {'type': DmapFieldType.DMAP_DICT, 'name': 'dpap.iphotoslideshowadvancedoptions'},
        'ipsl': {'type': DmapFieldType.DMAP_DICT, 'name': 'dpap.iphotoslideshowoptions'},
        'mbcl': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.bag'},
        'mccr': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.contentcodesresponse'},
        'mcna': {'type': DmapFieldType.DMAP_STR, 'name': 'dmap.contentcodesname'},
        'mcnm': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.contentcodesnumber'},
        'mcon': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.container'},
        'mctc': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.containercount'},
        'mcti': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.containeritemid'},
        'mcty': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.contentcodestype'},
        'mdbk': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.databasekind'},
        'mdcl': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.dictionary'},
        'mdst': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.downloadstatus'},
        'meds': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.editcommandssupported'},
        'miid': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.itemid'},
        'mikd': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.itemkind'},
        'mimc': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.itemcount'},
        'minm': {'type': DmapFieldType.DMAP_STR, 'name': 'dmap.itemname'},
        'mlcl': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.listing'},
        'mlid': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.sessionid'},
        'mlit': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.listingitem'},
        'mlog': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.loginresponse'},
        'mpco': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.parentcontainerid'},
        'mper': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.persistentid'},
        'mpro': {'type': DmapFieldType.DMAP_VERS, 'name': 'dmap.protocolversion'},
        'mrco': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.returnedcount'},
        'mrpr': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.remotepersistentid'},
        'msal': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportsautologout'},
        'msas': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.authenticationschemes'},
        'msau': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.authenticationmethod'},
        'msbr': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportsbrowse'},
        'msdc': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.databasescount'},
        'msex': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportsextensions'},
        'msix': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportsindex'},
        'mslr': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.loginrequired'},
        'msma': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.machineaddress'},
        'msml': {'type': DmapFieldType.DMAP_DICT, 'name': 'msml'},
        'mspi': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportspersistentids'},
        'msqy': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportsquery'},
        'msrs': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportsresolve'},
        'msrv': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.serverinforesponse'},
        'mstc': {'type': DmapFieldType.DMAP_DATE, 'name': 'dmap.utctime'},
        'mstm': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.timeoutinterval'},
        'msto': {'type': DmapFieldType.DMAP_INT, 'name': 'dmap.utcoffset'},
        'msts': {'type': DmapFieldType.DMAP_STR, 'name': 'dmap.statusstring'},
        'mstt': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.status'},
        'msup': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.supportsupdate'},
        'mtco': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.specifiedtotalcount'},
        'mudl': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.deletedidlisting'},
        'mupd': {'type': DmapFieldType.DMAP_DICT, 'name': 'dmap.updateresponse'},
        'musr': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.serverrevision'},
        'muty': {'type': DmapFieldType.DMAP_UINT, 'name': 'dmap.updatetype'},
        'pasp': {'type': DmapFieldType.DMAP_STR, 'name': 'dpap.aspectratio'},
        'pcmt': {'type': DmapFieldType.DMAP_STR, 'name': 'dpap.imagecomments'},
        'peak': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.photos.album-kind'},
        'peed': {'type': DmapFieldType.DMAP_DATE, 'name': 'com.apple.itunes.photos.exposure-date'},
        'pefc': {'type': DmapFieldType.DMAP_DICT, 'name': 'com.apple.itunes.photos.faces'},
        'peki': {'type': DmapFieldType.DMAP_UINT, 'name': 'com.apple.itunes.photos.key-image-id'},
        'pemd': {'type': DmapFieldType.DMAP_DATE, 'name': 'com.apple.itunes.photos.modification-date'},
        'pfai': {'type': DmapFieldType.DMAP_DICT, 'name': 'dpap.failureids'},
        'pfdt': {'type': DmapFieldType.DMAP_DICT, 'name': 'dpap.filedata'},
        'pfmt': {'type': DmapFieldType.DMAP_STR, 'name': 'dpap.imageformat'},
        'phgt': {'type': DmapFieldType.DMAP_UINT, 'name': 'dpap.imagepixelheight'},
        'picd': {'type': DmapFieldType.DMAP_DATE, 'name': 'dpap.creationdate'},
        'pifs': {'type': DmapFieldType.DMAP_UINT, 'name': 'dpap.imagefilesize'},
        'pimf': {'type': DmapFieldType.DMAP_STR, 'name': 'dpap.imagefilename'},
        'plsz': {'type': DmapFieldType.DMAP_UINT, 'name': 'dpap.imagelargefilesize'},
        'ppro': {'type': DmapFieldType.DMAP_VERS, 'name': 'dpap.protocolversion'},
        'prat': {'type': DmapFieldType.DMAP_UINT, 'name': 'dpap.imagerating'},
        'pret': {'type': DmapFieldType.DMAP_DICT, 'name': 'dpap.retryids'},
        'pwth': {'type': DmapFieldType.DMAP_UINT, 'name': 'dpap.imagepixelwidth'}
    }

    @classmethod
    def get(cls, code):
        return cls.data.get(code, None)

class DaapParser(object):
    @classmethod
    def to_uint(cls, daap_buffer, length):
        """In that case, ```length``` represents on how many bytes is the
        number coded
        """
        if length == 1:
            return DaapNumericReader.uint8(daap_buffer.read(length))
        elif length == 2:
            return DaapNumericReader.uint16(daap_buffer.read(length))
        elif length == 4:
            return DaapNumericReader.uint32(daap_buffer.read(length))
        elif length == 8:
            return DaapNumericReader.uint64(daap_buffer.read(length))

    @classmethod
    def to_int(cls, daap_buffer, length):
        if length == 1:
            return DaapNumericReader.int8(daap_buffer.read(length))
        elif length == 2:
            return DaapNumericReader.int16(daap_buffer.read(length))
        elif length == 4:
            return DaapNumericReader.int32(daap_buffer.read(length))
        elif length == 8:
            return DaapNumericReader.int64(daap_buffer.read(length))

    @classmethod
    def to_version(cls, daap_buffer, length):
        """It seems DAAP protocol uses always same pattern for versions
                xx.yy
        """    
        return '{}.{}'.format(
            DaapNumericReader.uint16(daap_buffer.read(2)),
            DaapNumericReader.uint16(daap_buffer.read(2)),
        )

    @classmethod
    def to_string(cls, daap_buffer, length):
        """Only read ```length``` bytes of ```daap_buffer``` to
        extract a string
        """
        return daap_buffer.read(length)

    @classmethod
    def to_dict(cls, daap_buffer, length):
        """Calling ```parse``` method kind of recursively to
        extract sub-dictionary
        """
        return cls.parse(DaapStringIO(daap_buffer.read(length)))

    @classmethod
    def parse(cls, daap_buffer, length=None):
        """Parse DAAP raw data to Python dictionary

        According some unofficial documentation and my tests,
        DAAP protocol is quite simple. In a RAW DAAP buffer, data is
        represented like this:
                From byte 0 to byte 3, instruction code
                From byte 4 to byte 7, content length of the instruction
                From byte 8 to ```length + 8```, content
        This is how the ```parse``` method proceed to convert
        ```daap_buffer``` into a human readable Python dictionary.
        """
        result = {}
        read_fct = {
            DmapFieldType.DMAP_UNKNOWN: cls.to_uint,
            DmapFieldType.DMAP_UINT: cls.to_uint,
            DmapFieldType.DMAP_INT: cls.to_int,
            DmapFieldType.DMAP_STR: cls.to_string,
            DmapFieldType.DMAP_DATA: cls.to_int,
            DmapFieldType.DMAP_DATE: cls.to_int,
            DmapFieldType.DMAP_VERS: cls.to_version,
            DmapFieldType.DMAP_DICT: cls.to_dict,
        }

        for code in iter(lambda: daap_buffer.read(4), ''):
            instruction = DmapInstruction.get(code)
            length = DaapNumericReader.uint32(daap_buffer.read(4))

            # Didn't find what the code is, try to guess what type is
            if not instruction:
                instruction = {
                    'type': DmapFieldType.DMAP_UNKNOWN,
                    'name': code,
                }

                # Check if buffer is four char code, then integer length
                if length >= 8:
                    s = daap_buffer.get_data(4)
                    if s.isalpha():
                        n = DaapNumericReader.uint32(daap_buffer.get_data(4, 4))
                        if n < length:
                            instruct['type'] = DmapFieldType.DMAP_DICT

                # Check if buffer has printable characters only
                if instruction['type'] == DmapFieldType.DMAP_UNKNOWN:
                    s = daap_buffer.get_data(length)
                    if all(c in string.printable for c in s):
                        instruction['type'] = DmapFieldType.DMAP_STR
                    else:
                        instruction['type'] = DmapFieldType.DMAP_UINT

            inst_name, inst_type = instruction['name'], instruction['type']

            if read_fct.get(inst_type, None):
                result[inst_name] = read_fct[inst_type](daap_buffer, length)
            else:
                raise DmapFieldNotFound(
                    '{} field type does not exist'.format(inst_type)
                )

        return result