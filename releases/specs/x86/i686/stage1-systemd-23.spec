subarch: i686
target: stage1
version_stamp: systemd-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/x86/23.0/i686/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-default/stage3-i686-systemd-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
