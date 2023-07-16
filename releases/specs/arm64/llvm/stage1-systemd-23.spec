subarch: arm64
target: stage1
version_stamp: llvm-systemd-@TIMESTAMP@
rel_type: 23.0-llvm
profile: default/linux/arm64/23.0/llvm/systemd
snapshot_treeish: @TIMESTAMP@
source_subpath: 23.0-llvm/stage3-arm64-llvm-systemd-latest.tar.xz
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
