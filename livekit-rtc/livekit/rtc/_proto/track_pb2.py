# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: track.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'track.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import e2ee_pb2 as e2ee__pb2
from . import handle_pb2 as handle__pb2
from . import stats_pb2 as stats__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btrack.proto\x12\rlivekit.proto\x1a\ne2ee.proto\x1a\x0chandle.proto\x1a\x0bstats.proto\">\n\x17\x43reateVideoTrackRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsource_handle\x18\x02 \x01(\x04\"D\n\x18\x43reateVideoTrackResponse\x12(\n\x05track\x18\x01 \x01(\x0b\x32\x19.livekit.proto.OwnedTrack\">\n\x17\x43reateAudioTrackRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rsource_handle\x18\x02 \x01(\x04\"D\n\x18\x43reateAudioTrackResponse\x12(\n\x05track\x18\x01 \x01(\x0b\x32\x19.livekit.proto.OwnedTrack\"\'\n\x0fGetStatsRequest\x12\x14\n\x0ctrack_handle\x18\x01 \x01(\x04\"$\n\x10GetStatsResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"j\n\x10GetStatsCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12&\n\x05stats\x18\x03 \x03(\x0b\x32\x17.livekit.proto.RtcStatsB\x08\n\x06_error\"\x0c\n\nTrackEvent\"\xa3\x02\n\x14TrackPublicationInfo\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\x04kind\x18\x03 \x01(\x0e\x32\x18.livekit.proto.TrackKind\x12*\n\x06source\x18\x04 \x01(\x0e\x32\x1a.livekit.proto.TrackSource\x12\x13\n\x0bsimulcasted\x18\x05 \x01(\x08\x12\r\n\x05width\x18\x06 \x01(\r\x12\x0e\n\x06height\x18\x07 \x01(\r\x12\x11\n\tmime_type\x18\x08 \x01(\t\x12\r\n\x05muted\x18\t \x01(\x08\x12\x0e\n\x06remote\x18\n \x01(\x08\x12\x36\n\x0f\x65ncryption_type\x18\x0b \x01(\x0e\x32\x1d.livekit.proto.EncryptionType\"y\n\x15OwnedTrackPublication\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12\x31\n\x04info\x18\x02 \x01(\x0b\x32#.livekit.proto.TrackPublicationInfo\"\x9f\x01\n\tTrackInfo\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\x04kind\x18\x03 \x01(\x0e\x32\x18.livekit.proto.TrackKind\x12\x30\n\x0cstream_state\x18\x04 \x01(\x0e\x32\x1a.livekit.proto.StreamState\x12\r\n\x05muted\x18\x05 \x01(\x08\x12\x0e\n\x06remote\x18\x06 \x01(\x08\"c\n\nOwnedTrack\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12&\n\x04info\x18\x02 \x01(\x0b\x32\x18.livekit.proto.TrackInfo\";\n\x15LocalTrackMuteRequest\x12\x14\n\x0ctrack_handle\x18\x01 \x01(\x04\x12\x0c\n\x04mute\x18\x02 \x01(\x08\"\'\n\x16LocalTrackMuteResponse\x12\r\n\x05muted\x18\x01 \x01(\x08\"A\n\x18\x45nableRemoteTrackRequest\x12\x14\n\x0ctrack_handle\x18\x01 \x01(\x04\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\",\n\x19\x45nableRemoteTrackResponse\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08*=\n\tTrackKind\x12\x10\n\x0cKIND_UNKNOWN\x10\x00\x12\x0e\n\nKIND_AUDIO\x10\x01\x12\x0e\n\nKIND_VIDEO\x10\x02*\x81\x01\n\x0bTrackSource\x12\x12\n\x0eSOURCE_UNKNOWN\x10\x00\x12\x11\n\rSOURCE_CAMERA\x10\x01\x12\x15\n\x11SOURCE_MICROPHONE\x10\x02\x12\x16\n\x12SOURCE_SCREENSHARE\x10\x03\x12\x1c\n\x18SOURCE_SCREENSHARE_AUDIO\x10\x04*D\n\x0bStreamState\x12\x11\n\rSTATE_UNKNOWN\x10\x00\x12\x10\n\x0cSTATE_ACTIVE\x10\x01\x12\x10\n\x0cSTATE_PAUSED\x10\x02\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'track_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_TRACKKIND']._serialized_start=1433
  _globals['_TRACKKIND']._serialized_end=1494
  _globals['_TRACKSOURCE']._serialized_start=1497
  _globals['_TRACKSOURCE']._serialized_end=1626
  _globals['_STREAMSTATE']._serialized_start=1628
  _globals['_STREAMSTATE']._serialized_end=1696
  _globals['_CREATEVIDEOTRACKREQUEST']._serialized_start=69
  _globals['_CREATEVIDEOTRACKREQUEST']._serialized_end=131
  _globals['_CREATEVIDEOTRACKRESPONSE']._serialized_start=133
  _globals['_CREATEVIDEOTRACKRESPONSE']._serialized_end=201
  _globals['_CREATEAUDIOTRACKREQUEST']._serialized_start=203
  _globals['_CREATEAUDIOTRACKREQUEST']._serialized_end=265
  _globals['_CREATEAUDIOTRACKRESPONSE']._serialized_start=267
  _globals['_CREATEAUDIOTRACKRESPONSE']._serialized_end=335
  _globals['_GETSTATSREQUEST']._serialized_start=337
  _globals['_GETSTATSREQUEST']._serialized_end=376
  _globals['_GETSTATSRESPONSE']._serialized_start=378
  _globals['_GETSTATSRESPONSE']._serialized_end=414
  _globals['_GETSTATSCALLBACK']._serialized_start=416
  _globals['_GETSTATSCALLBACK']._serialized_end=522
  _globals['_TRACKEVENT']._serialized_start=524
  _globals['_TRACKEVENT']._serialized_end=536
  _globals['_TRACKPUBLICATIONINFO']._serialized_start=539
  _globals['_TRACKPUBLICATIONINFO']._serialized_end=830
  _globals['_OWNEDTRACKPUBLICATION']._serialized_start=832
  _globals['_OWNEDTRACKPUBLICATION']._serialized_end=953
  _globals['_TRACKINFO']._serialized_start=956
  _globals['_TRACKINFO']._serialized_end=1115
  _globals['_OWNEDTRACK']._serialized_start=1117
  _globals['_OWNEDTRACK']._serialized_end=1216
  _globals['_LOCALTRACKMUTEREQUEST']._serialized_start=1218
  _globals['_LOCALTRACKMUTEREQUEST']._serialized_end=1277
  _globals['_LOCALTRACKMUTERESPONSE']._serialized_start=1279
  _globals['_LOCALTRACKMUTERESPONSE']._serialized_end=1318
  _globals['_ENABLEREMOTETRACKREQUEST']._serialized_start=1320
  _globals['_ENABLEREMOTETRACKREQUEST']._serialized_end=1385
  _globals['_ENABLEREMOTETRACKRESPONSE']._serialized_start=1387
  _globals['_ENABLEREMOTETRACKRESPONSE']._serialized_end=1431
# @@protoc_insertion_point(module_scope)
