subarch: rv64_multilib
target: stage1
version_stamp: openrc-@TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64 /usr/bin/qemu-riscv32
rel_type: default
profile: default/linux/riscv/20.0/rv64gc/multilib
snapshot_treeish: @TIMESTAMP@
source_subpath: default/stage3-rv64_multilib-openrc-latest
compression_mode: pixz
decompressor_search_order: xz bzip2
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
