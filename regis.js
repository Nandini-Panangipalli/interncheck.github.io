let registeredUsers = [];

    function exportToExcel() {
      const wb = XLSX.utils.book_new();
      const ws = XLSX.utils.json_to_sheet(registeredUsers);
      XLSX.utils.book_append_sheet(wb, ws, 'Registered Users');
      const wbout = XLSX.write(wb, { bookType: 'xlsx', type: 'binary' });

      function s2ab(s) {
        const buf = new ArrayBuffer(s.length);
        const view = new Uint8Array(buf);
        for (let i = 0; i < s.length; i++) view[i] = s.charCodeAt(i) & 0xff;
        return buf;
      }

      const blob = new Blob([s2ab(wbout)], { type: 'application/octet-stream' });
      const link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.download = 'registered_users.xlsx';
      link.click();
    }

    const registerForm = document.getElementById('registerForm');

    registerForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const ftname = document.getElementById('fname').value;
      const lname = document.getElementById('lname').value;
      const email = document.getElementById('email').value;
      const age = document.getElementById('age').value;
      const number = document.getElementById('number').value;
      const pass = document.getElementById('pass').value;
      const passd = document.getElementById('passd').value;

      const user = { fname , lname , email , age, number , pass, passd} ;

      // Save the user to the array
      registeredUsers.push(user);

      // Reset form inputs
      document.getElementById('fname').value = '';
      document.getElementById('lname').value = '';
      document.getElementById('email').value = '';
      document.getElementById('age').value = '';
      document.getElementById('number').value = '';
      document.getElementById('pass').value = '';
      document.getElementById('passd').value = '';
    });

    window.addEventListener('beforeunload', function (e) {
      // Export the registered users to Excel when the page is closed or refreshed
      if (registeredUsers.length > 0) {
        exportToExcel();
      }
    });