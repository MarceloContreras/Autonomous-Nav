
"use strict";

let CompositeDetectedPersons = require('./CompositeDetectedPersons.js');
let DetectedPerson = require('./DetectedPerson.js');
let PersonTrajectory = require('./PersonTrajectory.js');
let CompositeDetectedPerson = require('./CompositeDetectedPerson.js');
let PersonTrajectoryEntry = require('./PersonTrajectoryEntry.js');
let TrackedGroups = require('./TrackedGroups.js');
let TrackedPerson = require('./TrackedPerson.js');
let DetectedPersons = require('./DetectedPersons.js');
let TrackedPersons = require('./TrackedPersons.js');
let ImmDebugInfo = require('./ImmDebugInfo.js');
let TrackedPersons2d = require('./TrackedPersons2d.js');
let TrackingTimingMetrics = require('./TrackingTimingMetrics.js');
let TrackedGroup = require('./TrackedGroup.js');
let ImmDebugInfos = require('./ImmDebugInfos.js');
let TrackedPerson2d = require('./TrackedPerson2d.js');

module.exports = {
  CompositeDetectedPersons: CompositeDetectedPersons,
  DetectedPerson: DetectedPerson,
  PersonTrajectory: PersonTrajectory,
  CompositeDetectedPerson: CompositeDetectedPerson,
  PersonTrajectoryEntry: PersonTrajectoryEntry,
  TrackedGroups: TrackedGroups,
  TrackedPerson: TrackedPerson,
  DetectedPersons: DetectedPersons,
  TrackedPersons: TrackedPersons,
  ImmDebugInfo: ImmDebugInfo,
  TrackedPersons2d: TrackedPersons2d,
  TrackingTimingMetrics: TrackingTimingMetrics,
  TrackedGroup: TrackedGroup,
  ImmDebugInfos: ImmDebugInfos,
  TrackedPerson2d: TrackedPerson2d,
};
