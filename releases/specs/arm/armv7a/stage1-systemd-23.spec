subarch: armv7a
version_stamp: systemd-@TIMESTAMP@
target: stage1
rel_type: 23.0-default
profile: default/linux/arm/23.0/armv7a_sf/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-default/stage3-armv7a-systemd-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
