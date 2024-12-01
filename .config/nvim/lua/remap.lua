-- Navigate/Split windows
vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)
vim.keymap.set("n", "<leader>vs", vim.cmd.vsplit)
vim.keymap.set("n", "<leader>hs", vim.cmd.split)

vim.keymap.set("n", "<Tab>", "<C-w>w")
vim.keymap.set("n", "<C-i>", "<C-w>+")
vim.keymap.set("n", "<C-k>", "<C-w>-")
vim.keymap.set("n", "<C-j>", "<C-w><")
vim.keymap.set("n", "<C-l>", "<C-w>>")

-- Toggle xxd hexdump to allow binary patching
vim.keymap.set("n", "<C-Tab>", function() toggle_hex_dump() end)
vim.g.hexdump = false
function toggle_hex_dump()
    if vim.g.hexdump then
        vim.cmd("%!xxd -r")
        vim.g.hexdump = false
        return
    end
    vim.cmd("%!xxd")
    vim.g.hexdump = true
end
