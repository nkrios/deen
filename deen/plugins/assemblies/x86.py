try:
    import keystone
    import capstone
    KEYSTONE = True
except ImportError:
    KEYSTONE = False

from .__base__ import AsmBase


class DeenPluginAsmX86(AsmBase):
    name = 'assembly_x86'
    display_name = 'x86'
    aliases = ['asm_x86',
               'asmx86',
               'assemble_x86',
               'assemblex86',
               'x86']
    cmd_name = 'assembly_x86'
    cmd_help='Assemble/Disassemble for the x86 architecture'
    keystone_arch = keystone.KS_ARCH_X86
    keystone_mode = keystone.KS_MODE_32
    capstone_arch = capstone.CS_ARCH_X86
    capstone_mode = capstone.CS_MODE_32


class DeenPluginAsmX86_64(AsmBase):
    name = 'assembly_x86_64'
    display_name = 'x86_64'
    aliases = ['asm_x86_64',
               'asmx86_64',
               'x86_64',
               'x64']
    cmd_name = 'assembly_x86_64'
    cmd_help='Assemble/Disassemble for the x86_64 architecture'
    keystone_arch = keystone.KS_ARCH_X86
    keystone_mode = keystone.KS_MODE_64
    capstone_arch = capstone.CS_ARCH_X86
    capstone_mode = capstone.CS_MODE_64
