# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .v1_api_group import V1APIGroup
from .v1_api_group_list import V1APIGroupList
from .v1_api_resource import V1APIResource
from .v1_api_resource_list import V1APIResourceList
from .v1_affinity import V1Affinity
from .v1_cd_rom_target import V1CDRomTarget
from .v1_cpu import V1CPU
from .v1_clock import V1Clock
from .v1_clock_offset_utc import V1ClockOffsetUTC
from .v1_cloud_init_no_cloud_source import V1CloudInitNoCloudSource
from .v1_delete_options import V1DeleteOptions
from .v1_devices import V1Devices
from .v1_disk import V1Disk
from .v1_disk_target import V1DiskTarget
from .v1_domain_spec import V1DomainSpec
from .v1_empty_disk_source import V1EmptyDiskSource
from .v1_ephemeral_volume_source import V1EphemeralVolumeSource
from .v1_feature_apic import V1FeatureAPIC
from .v1_feature_hyperv import V1FeatureHyperv
from .v1_feature_spinlocks import V1FeatureSpinlocks
from .v1_feature_state import V1FeatureState
from .v1_feature_vendor_id import V1FeatureVendorID
from .v1_features import V1Features
from .v1_firmware import V1Firmware
from .v1_floppy_target import V1FloppyTarget
from .v1_group_version_for_discovery import V1GroupVersionForDiscovery
from .v1_hpet_timer import V1HPETTimer
from .v1_hyperv_timer import V1HypervTimer
from .v1_i6300_esb_watchdog import V1I6300ESBWatchdog
from .v1_initializer import V1Initializer
from .v1_initializers import V1Initializers
from .v1_interface import V1Interface
from .v1_kvm_timer import V1KVMTimer
from .v1_label_selector import V1LabelSelector
from .v1_label_selector_requirement import V1LabelSelectorRequirement
from .v1_list_meta import V1ListMeta
from .v1_local_object_reference import V1LocalObjectReference
from .v1_lun_target import V1LunTarget
from .v1_machine import V1Machine
from .v1_network import V1Network
from .v1_node_affinity import V1NodeAffinity
from .v1_node_selector import V1NodeSelector
from .v1_node_selector_requirement import V1NodeSelectorRequirement
from .v1_node_selector_term import V1NodeSelectorTerm
from .v1_object_meta import V1ObjectMeta
from .v1_offline_virtual_machine import V1OfflineVirtualMachine
from .v1_offline_virtual_machine_condition import V1OfflineVirtualMachineCondition
from .v1_offline_virtual_machine_list import V1OfflineVirtualMachineList
from .v1_offline_virtual_machine_spec import V1OfflineVirtualMachineSpec
from .v1_offline_virtual_machine_status import V1OfflineVirtualMachineStatus
from .v1_owner_reference import V1OwnerReference
from .v1_pit_timer import V1PITTimer
from .v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from .v1_pod_affinity import V1PodAffinity
from .v1_pod_affinity_term import V1PodAffinityTerm
from .v1_pod_anti_affinity import V1PodAntiAffinity
from .v1_preconditions import V1Preconditions
from .v1_preferred_scheduling_term import V1PreferredSchedulingTerm
from .v1_rtc_timer import V1RTCTimer
from .v1_registry_disk_source import V1RegistryDiskSource
from .v1_resource_requirements import V1ResourceRequirements
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from .v1_status import V1Status
from .v1_status_cause import V1StatusCause
from .v1_status_details import V1StatusDetails
from .v1_timer import V1Timer
from .v1_vm_replica_set_condition import V1VMReplicaSetCondition
from .v1_vm_replica_set_spec import V1VMReplicaSetSpec
from .v1_vm_replica_set_status import V1VMReplicaSetStatus
from .v1_vm_template_spec import V1VMTemplateSpec
from .v1_virtual_machine import V1VirtualMachine
from .v1_virtual_machine_condition import V1VirtualMachineCondition
from .v1_virtual_machine_list import V1VirtualMachineList
from .v1_virtual_machine_network_interface import V1VirtualMachineNetworkInterface
from .v1_virtual_machine_preset import V1VirtualMachinePreset
from .v1_virtual_machine_preset_list import V1VirtualMachinePresetList
from .v1_virtual_machine_preset_spec import V1VirtualMachinePresetSpec
from .v1_virtual_machine_replica_set import V1VirtualMachineReplicaSet
from .v1_virtual_machine_replica_set_list import V1VirtualMachineReplicaSetList
from .v1_virtual_machine_spec import V1VirtualMachineSpec
from .v1_virtual_machine_status import V1VirtualMachineStatus
from .v1_volume import V1Volume
from .v1_watch_event import V1WatchEvent
from .v1_watchdog import V1Watchdog
from .v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm
