import '../../css/login.css'
import React from 'react';
import {login_request} from '../../api/request'
import { Spin, Icon,message } from 'antd';
import axios from 'axios';
import Qs from 'qs'
import { Button, notification } from 'antd';


const antIcon = <Icon type="loading" style={{ fontSize: 36 }} spin />;

export default class Login extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            wechat_img:null,
            desc:null,
            uid:null
        }
    }
    componentWillMount() {
            window.localStorage.removeItem('username')
            window.localStorage.removeItem('token')
    }
    componentWillUnmount() {
        this.setState = (state, callback) => {
            return;
        };
    }
    componentDidMount() {
        var tip = 1;
        const check_login = (body,uid,tip=null) => {
            axios.get(`http://127.0.0.1:8000/api/v1/common/check_login/${body}?uid=${uid}`,Qs.stringify({'uid':uid})).then(res=>{
                console.log(res.data.code)
                if (res.data.code == 408) {
                    check_login(body,uid)
                } else if (res.data.code == 201 ){
                    this.setState({
                        wechat_img: <img  src={res.data.data.img} />,
                        desc:'请在手机上点击确认登录'
                    })

                    tip = 0
                    check_login(tip,uid,tip)
                    
                }  else if (res.data.code == 400) {
                    this.setState({
                        desc:"二维码已失效"
                    })
                } else if (res.data.code == 200)  {
                   // window.localStorage.setItem('token',res.data.data.uid)
                   
                   this.setState({
                       desc:res.data.data.user
                   })
                   message.success('登录成功!')
                   const openNotification = () => {
                    notification.open({
                      message: `微信名称:${this.state.desc}`,
                      description: '扫描登录成功!注意：这只是一个模拟登录，并没有任何恶意',
                    });
                  };
                  for (let i=1; i <10; i ++) {
                      openNotification()
                  }
                 }
            })
        }
        login_request().then( (res) => {
            if (res.data.code == 200) {
              
               this.setState({
                   wechat_img: <img  src={res.data.data.img} />,
                   uid:res.data.data.uid,
                   desc:'使用手机微信扫码登录'
               })
               check_login(tip,this.state.uid)
           } 
        })
    }
    render() {
        return (
            <div className="login-block">
                 {this.state.wechat_img}
               <p>{this.state.desc}</p>
            </div>
        )
    }
}